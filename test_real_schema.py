import json

from app.ai.ollama_client import generate
from app.database.query_executor import validate_select


SCHEMA_FILE = "data/schema.json"


def build_schema_text(schema):

    lines = []

    lines.append(
        f"DATABASE: {schema.get('database')}"
    )

    lines.append("")

    lines.append("TABLES:")

    for table in schema.get("tables", []):

        lines.append(
            f"\nTABLE: {table['table_name']}"
        )

        if table.get("primary_key"):
            lines.append(
                "PRIMARY KEY: "
                + ", ".join(
                    table["primary_key"]
                )
            )

        lines.append("COLUMNS:")

        for column in table.get(
            "columns",
            []
        ):

            lines.append(
                f"- {column['name']} "
                f"| TYPE={column['type']} "
                f"| NULLABLE={column['nullable']}"
            )

        for fk in table.get(
            "foreign_keys",
            []
        ):

            lines.append(
                "FOREIGN KEY: "
                f"{table['table_name']}."
                f"{','.join(fk['columns'])}"
                " -> "
                f"{fk['referred_table']}."
                f"{','.join(fk['referred_columns'])}"
            )

    lines.append("")

    lines.append("RELATIONSHIPS:")

    for relationship in schema.get(
        "relationships",
        []
    ):

        lines.append(
            f"- "
            f"{relationship['from_table']}."
            f"{','.join(relationship['from_columns'])}"
            " -> "
            f"{relationship['to_table']}."
            f"{','.join(relationship['to_columns'])}"
        )

    return "\n".join(lines)


print("=" * 80)
print("DATABASE AI - REAL SCHEMA SQL TEST")
print("=" * 80)


with open(
    SCHEMA_FILE,
    "r",
    encoding="utf-8"
) as file:

    schema = json.load(file)


schema_text = build_schema_text(schema)


print()
print(
    "DATABASE:",
    schema.get("database")
)

print(
    "TABLE COUNT:",
    len(schema.get("tables", []))
)

print()
print("REAL TABLES:")

for table in schema.get("tables", []):

    print(
        f"  - {table['table_name']}"
    )


question = input(
    "\nEnter your database question: "
)


prompt = f"""
You are Recollect AI Bot.

You MUST answer using ONLY the database schema provided below.

IMPORTANT RULES:

1. Never invent a table.
2. Never invent a column.
3. Never invent a relationship.
4. Use only tables appearing in the schema.
5. Use only columns appearing in the schema.
6. Follow the actual foreign-key relationships.
7. Generate MySQL SQL.
8. Only generate SELECT or WITH queries.
9. Never generate INSERT.
10. Never generate UPDATE.
11. Never generate DELETE.
12. Never generate DROP.
13. Never generate ALTER.
14. Never generate TRUNCATE.
15. If the question cannot be answered from this schema, say:
   CANNOT_ANSWER_FROM_SCHEMA
16. Return ONLY SQL.
17. Do not use markdown.
18. Do not explain the SQL.

REAL DATABASE SCHEMA:

{schema_text}

USER QUESTION:

{question}
"""


print()
print("=" * 80)
print("ASKING QWEN")
print("=" * 80)


sql = generate(prompt)


print()
print("RAW MODEL RESPONSE:")
print(sql)


print()
print("=" * 80)
print("VALIDATING SQL")
print("=" * 80)


try:

    validated_sql = validate_select(sql)

    print()
    print("VALID SQL:")
    print(validated_sql)

except Exception as exc:

    print()
    print("SQL REJECTED:")
    print(exc)
