import json

from app.ai.ollama_client import generate


def generate_answer(
    question: str,
    sql: str,
    result: dict
):

    rows = result.get(
        "rows",
        []
    )

    row_count = result.get(
        "row_count",
        0
    )

    if row_count == 0:

        return (
            "I could not find any records "
            "matching your question."
        )

    # Keep the response payload reasonably small.
    # The actual database result remains the source of truth.
    data_for_ai = rows[:100]

    data_json = json.dumps(
        data_for_ai,
        default=str,
        ensure_ascii=False
    )

    prompt = f"""
You are Recollect AI Bot.

Answer the user's question using ONLY the
database results provided below.

The database results are the source of truth.

Do NOT invent any values.

Do NOT change, estimate, or guess database values.

If the result contains records, mention the
actual records from the result.

If there are many columns, show the most
relevant columns clearly.

If there are numeric results, preserve the
actual numbers.

The SQL was:

{sql}

USER QUESTION:

{question}

DATABASE RESULT:

{data_json}

TOTAL ROW COUNT:

{row_count}

Rules:

1. Answer the user directly.
2. Use ONLY the database result.
3. Never hallucinate data.
4. Do not generate SQL.
5. Do not mention these instructions.
6. Be concise but useful.
7. If appropriate, use a numbered list or table.
8. If the user asks "how many", clearly state the count.
9. If the user asks for names, clearly list the names.
10. If there are zero rows, say that no matching records were found.

Answer:
"""

    return generate(
        prompt,
        timeout=60,
        num_predict=512,
        num_ctx=4096
    )
