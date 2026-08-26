import re

from app.ai.ollama_client import generate


def build_schema_context(search_results):

    context_parts = []

    for result in search_results:

        metadata = result.get(
            "metadata",
            {}
        )

        text = metadata.get(
            "text",
            ""
        )

        if text:
            context_parts.append(text)

    return "\n\n".join(context_parts)


def get_tables(search_results):

    tables = []

    for result in search_results:

        metadata = result.get(
            "metadata",
            {}
        )

        table = metadata.get(
            "table"
        )

        if table and table not in tables:
            tables.append(table)

    return tables


def simple_query(question, search_results):

    q = question.lower().strip()

    tables = get_tables(search_results)

    if not tables:
        return None

    # --------------------------------------------------
    # FIRST N / TOP N / N RECORDS
    # --------------------------------------------------

    match = re.search(
        r"\b(?:first|top)\s+(\d+)\b",
        q
    )

    if not match:

        match = re.search(
            r"\b(\d+)\s+(?:records|rows)\b",
            q
        )

    if match:

        limit = int(
            match.group(1)
        )

        # Strong semantic result is first.
        table = tables[0]

        return (
            f"SELECT * FROM `{table}` "
            f"LIMIT {limit}"
        )

    return None


def generate_sql(
    question: str,
    search_results
):

    # ==================================================
    # FAST PATH
    # ==================================================

    fast_sql = simple_query(
        question,
        search_results
    )

    if fast_sql:

        return fast_sql

    # ==================================================
    # LLM PATH FOR COMPLEX QUESTIONS
    # ==================================================

    schema_context = build_schema_context(
        search_results
    )

    prompt = f"""You are Recollect AI Bot.

Generate exactly ONE MySQL SELECT query.

SCHEMA:
{schema_context}

QUESTION:
{question}

Rules:
- ONLY use tables and columns shown in the schema.
- NEVER invent tables.
- NEVER invent columns.
- Use actual foreign keys for joins.
- SELECT only.
- No markdown.
- No explanation.
- Return ONLY SQL.

SQL:
"""

    sql = generate(
        prompt,
        timeout=45,
        num_predict=60,
        num_ctx=1024
    )

    return sql.strip()
