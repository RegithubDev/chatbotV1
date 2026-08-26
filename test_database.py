import json

from app.database.connector import (
    create_mysql_engine,
    test_connection,
    get_database_name,
    get_server_version,
)

from app.database.schema_reader import (
    read_schema,
    schema_summary,
)


# =========================================================
# DATABASE CONFIGURATION
# =========================================================

HOST = "localhost"
PORT = 3306
DATABASE = "aakridb"
USERNAME = "root"
PASSWORD = "Sai@12345"


# =========================================================
# CONNECT
# =========================================================

print()
print("=" * 70)
print("DATABASE AI - DATABASE CONNECTION TEST")
print("=" * 70)

engine = create_mysql_engine(
    host=HOST,
    port=PORT,
    database=DATABASE,
    username=USERNAME,
    password=PASSWORD,
)

print()
print("Testing connection...")

if not test_connection(engine):

    raise RuntimeError(
        "Database connection failed"
    )

print("? Database connection successful")


# =========================================================
# SERVER
# =========================================================

print()
print(
    "Database:",
    get_database_name(engine)
)

print(
    "Server:",
    get_server_version(engine)
)


# =========================================================
# READ COMPLETE SCHEMA
# =========================================================

print()
print("Reading complete database schema...")

schema = read_schema(
    engine,
    DATABASE
)

summary = schema_summary(
    schema
)


# =========================================================
# SUMMARY
# =========================================================

print()
print("=" * 70)
print("DATABASE SUMMARY")
print("=" * 70)

print(
    "Database:",
    summary["database"]
)

print(
    "Tables:",
    summary["table_count"]
)

print(
    "Columns:",
    summary["column_count"]
)

print(
    "Foreign Keys:",
    summary["foreign_key_count"]
)

print(
    "Relationships:",
    summary["relationship_count"]
)


# =========================================================
# TABLES
# =========================================================

print()
print("=" * 70)
print("TABLES")
print("=" * 70)

for table in schema["tables"]:

    print()
    print(
        "TABLE:",
        table["table_name"]
    )

    print(
        "ROWS:",
        table["row_count"]
    )

    print(
        "PRIMARY KEY:",
        table["primary_key"]
    )

    print(
        "COLUMNS:"
    )

    for column in table["columns"]:

        print(
            f"  - {column['name']} "
            f"| {column['type']} "
            f"| nullable={column['nullable']} "
            f"| PK={column['primary_key']}"
        )

    if table["foreign_keys"]:

        print(
            "FOREIGN KEYS:"
        )

        for fk in table["foreign_keys"]:

            print(
                f"  - {fk['columns']} "
                f"-> "
                f"{fk['referred_table']}"
                f"{fk['referred_columns']}"
            )


# =========================================================
# RELATIONSHIPS
# =========================================================

print()
print("=" * 70)
print("RELATIONSHIPS")
print("=" * 70)

for relationship in schema["relationships"]:

    print(
        f"{relationship['from_table']}"
        f".{relationship['from_columns']}"
        f" -> "
        f"{relationship['to_table']}"
        f".{relationship['to_columns']}"
    )


# =========================================================
# SAVE SCHEMA
# =========================================================

with open(
    "data/schema.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        schema,
        file,
        indent=2,
        default=str
    )


print()
print("=" * 70)
print("SCHEMA SAVED")
print("=" * 70)

print(
    "data/schema.json"
)

print()
print("DATABASE SCAN COMPLETE")
print()
