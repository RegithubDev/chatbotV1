from sqlalchemy import inspect, text
from sqlalchemy.engine import Engine


def read_schema(
    engine: Engine,
    database_name: str = None
):

    inspector = inspect(engine)

    if database_name is None:
        try:
            with engine.connect() as connection:
                database_name = connection.execute(
                    text("SELECT DATABASE()")
                ).scalar()
        except Exception:
            database_name = None

    tables = inspector.get_table_names()

    schema = {
        "database": database_name,
        "table_count": len(tables),
        "tables": [],
        "relationships": [],
    }

    for table_name in tables:

        columns = inspector.get_columns(table_name)

        pk_info = inspector.get_pk_constraint(
            table_name
        )

        foreign_keys = inspector.get_foreign_keys(
            table_name
        )

        indexes = inspector.get_indexes(
            table_name
        )

        primary_keys = pk_info.get(
            "constrained_columns",
            []
        )

        table_info = {
            "table_name": table_name,
            "columns": [],
            "primary_key": primary_keys,
            "foreign_keys": [],
            "indexes": [],
            "row_count": None,
        }

        # ==================================================
        # COLUMNS
        # ==================================================

        for column in columns:

            default_value = column.get("default")

            table_info["columns"].append({

                "name": column["name"],

                "type": str(
                    column["type"]
                ),

                "nullable": column.get(
                    "nullable",
                    True
                ),

                "default": (
                    str(default_value)
                    if default_value is not None
                    else None
                ),

                "primary_key": (
                    column["name"] in primary_keys
                ),

                "autoincrement": (
                    column.get(
                        "autoincrement"
                    )
                    is True
                ),

            })

        # ==================================================
        # FOREIGN KEYS
        # ==================================================

        for fk in foreign_keys:

            constrained_columns = fk.get(
                "constrained_columns",
                []
            )

            referred_columns = fk.get(
                "referred_columns",
                []
            )

            referred_table = fk.get(
                "referred_table"
            )

            fk_info = {

                "columns": constrained_columns,

                "referred_table":
                    referred_table,

                "referred_columns":
                    referred_columns,

                "name":
                    fk.get("name"),

            }

            table_info[
                "foreign_keys"
            ].append(
                fk_info
            )

            # ==============================================
            # GLOBAL RELATIONSHIP
            # ==============================================

            schema[
                "relationships"
            ].append({

                "from_table":
                    table_name,

                "from_columns":
                    constrained_columns,

                "to_table":
                    referred_table,

                "to_columns":
                    referred_columns,

                "foreign_key":
                    fk.get("name"),

            })

        # ==================================================
        # INDEXES
        # ==================================================

        for index in indexes:

            table_info[
                "indexes"
            ].append({

                "name":
                    index.get("name"),

                "columns":
                    index.get(
                        "column_names",
                        []
                    ),

                "unique":
                    index.get(
                        "unique",
                        False
                    ),

            })

        # ==================================================
        # ROW COUNT
        # ==================================================

        try:

            with engine.connect() as connection:

                result = connection.execute(
                    text(
                        f"SELECT COUNT(*) FROM `{table_name}`"
                    )
                )

                table_info["row_count"] = result.scalar()

        except Exception as exc:

            table_info["row_count_error"] = str(
                exc
            )

        # ==================================================
        # ADD TABLE
        # ==================================================

        schema[
            "tables"
        ].append(
            table_info
        )

    return schema


def schema_summary(schema: dict) -> dict:

    tables = schema.get(
        "tables",
        []
    )

    relationships = schema.get(
        "relationships",
        []
    )

    total_columns = sum(
        len(table.get("columns", []))
        for table in tables
    )

    total_foreign_keys = sum(
        len(table.get("foreign_keys", []))
        for table in tables
    )

    return {

        "database":
            schema.get("database"),

        "table_count":
            len(tables),

        "column_count":
            total_columns,

        "foreign_key_count":
            total_foreign_keys,

        "relationship_count":
            len(relationships),

        "tables":
            [
                table["table_name"]
                for table in tables
            ],

    }
