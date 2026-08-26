import json
from pathlib import Path


SCHEMA_DIRECTORY = Path(
    "data/schemas"
)


def save_schema(
    database_name: str,
    schema: dict
):

    SCHEMA_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = (
        SCHEMA_DIRECTORY
        / f"{database_name}.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            schema,
            file,
            indent=2,
            default=str
        )

    return str(file_path)


def load_schema(
    database_name: str
):

    file_path = (
        SCHEMA_DIRECTORY
        / f"{database_name}.json"
    )

    if not file_path.exists():

        return None

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)