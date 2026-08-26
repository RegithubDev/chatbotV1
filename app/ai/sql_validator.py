import re
import json
from pathlib import Path


FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE",
    "RENAME",
    "EXEC",
    "CALL"
]


SCHEMA_PATH = (
    Path(__file__).resolve()
    .parents[2]
    / "data"
    / "schemas"
    / "aakridb.json"
)


def load_schema():

    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(
            f"Schema file not found: {SCHEMA_PATH}"
        )

    with open(
        SCHEMA_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def get_schema_objects():

    schema = load_schema()

    tables = {}
    relationships = []

    for table in schema.get("tables", []):

        table_name = table.get(
            "table_name"
        )

        if not table_name:
            continue

        columns = set()

        for column in table.get(
            "columns",
            []
        ):

            name = column.get("name")

            if name:
                columns.add(
                    name.lower()
                )

        tables[
            table_name.lower()
        ] = {
            "name": table_name,
            "columns": columns
        }

    for relationship in schema.get(
        "relationships",
        []
    ):

        relationships.append(
            relationship
        )

    return tables, relationships


def clean_sql(sql: str):

    if not sql:
        return ""

    sql = sql.strip()

    # Remove markdown fences
    sql = re.sub(
        r"^```(?:sql)?\s*",
        "",
        sql,
        flags=re.IGNORECASE
    )

    sql = re.sub(
        r"\s*```\s*$",
        "",
        sql,
        flags=re.IGNORECASE
    )

    # Remove leading SQL label occasionally
    sql = re.sub(
        r"^\s*SQL\s*:\s*",
        "",
        sql,
        flags=re.IGNORECASE
    )

    return sql.strip()


def extract_table_names(sql):

    tables = []

    patterns = [
        r"\bFROM\s+([`A-Za-z_][\w$]*)",
        r"\bJOIN\s+([`A-Za-z_][\w$]*)",
        r"\bUPDATE\s+([`A-Za-z_][\w$]*)",
        r"\bINTO\s+([`A-Za-z_][\w$]*)"
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            sql,
            flags=re.IGNORECASE
        )

        for table in matches:

            table = table.strip("`")

            if table.lower() not in [
                x.lower()
                for x in tables
            ]:

                tables.append(table)

    return tables


def validate_tables(sql):

    tables, _ = get_schema_objects()

    referenced_tables = extract_table_names(
        sql
    )

    unknown_tables = []

    for table in referenced_tables:

        if table.lower() not in tables:

            unknown_tables.append(
                table
            )

    if unknown_tables:

        return {
            "valid": False,
            "reason": (
                "Unknown table(s): "
                + ", ".join(
                    unknown_tables
                )
            ),
            "unknown_tables": unknown_tables
        }

    return {
        "valid": True,
        "tables": referenced_tables
    }


def validate_sql(
    sql: str,
    strict_schema=True
):

    cleaned = clean_sql(
        sql
    )

    if not cleaned:

        return {
            "valid": False,
            "reason": "Empty SQL"
        }

    # Only one SQL statement
    statements = [
        statement.strip()
        for statement in cleaned.split(";")
        if statement.strip()
    ]

    if len(statements) > 1:

        return {
            "valid": False,
            "reason": "Multiple SQL statements are not allowed"
        }

    upper_sql = cleaned.upper()

    # Dangerous keywords
    for keyword in FORBIDDEN_KEYWORDS:

        if re.search(
            rf"\b{keyword}\b",
            upper_sql
        ):

            return {
                "valid": False,
                "reason": (
                    f"Forbidden SQL keyword: "
                    f"{keyword}"
                )
            }

    # SELECT / WITH only
    if not re.match(
        r"^\s*(SELECT|WITH)\b",
        upper_sql,
        re.IGNORECASE
    ):

        return {
            "valid": False,
            "reason": (
                "Only SELECT or WITH queries "
                "are allowed"
            )
        }

    # Schema validation
    if strict_schema:

        table_result = validate_tables(
            cleaned
        )

        if not table_result["valid"]:

            return table_result

    return {
        "valid": True,
        "sql": cleaned,
        "tables": extract_table_names(
            cleaned
        )
    }
