from sqlalchemy import text
from sqlalchemy.engine import Engine


def execute_select(
    engine: Engine,
    sql: str
):

    sql = sql.strip()

    with engine.connect() as connection:

        result = connection.execute(
            text(sql)
        )

        columns = list(
            result.keys()
        )

        rows = result.fetchall()

        data = []

        for row in rows:

            item = {}

            for column, value in zip(
                columns,
                row
            ):
                item[column] = value

            data.append(item)

        return {
            "columns": columns,
            "rows": data,
            "row_count": len(data)
        }
