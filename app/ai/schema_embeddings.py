from app.ai.ollama_client import embed

from app.vectorstore.faiss_store import create_index


def build_schema_documents(schema):

    documents = []

    for table in schema.get(
        "tables",
        []
    ):

        table_name = table[
            "table_name"
        ]

        columns = table.get(
            "columns",
            []
        )

        primary_keys = table.get(
            "primary_key",
            []
        )

        foreign_keys = table.get(
            "foreign_keys",
            []
        )

        column_text = []

        for column in columns:

            column_text.append(
                f"{column['name']} "
                f"{column['type']}"
            )

        fk_text = []

        for fk in foreign_keys:

            fk_text.append(
                f"{fk['columns']} references "
                f"{fk['referred_table']}."
                f"{fk['referred_columns']}"
            )

        text = (
            f"Table: {table_name}\n"
            f"Columns: "
            f"{', '.join(column_text)}\n"
            f"Primary keys: "
            f"{', '.join(primary_keys)}\n"
            f"Foreign keys: "
            f"{'; '.join(fk_text)}"
        )

        documents.append({

            "table": table_name,

            "text": text,

            "foreign_keys": foreign_keys

        })

    return documents


def build_embeddings(schema):

    documents = build_schema_documents(
        schema
    )

    embeddings = []

    metadata = []

    for document in documents:

        vector = embed(
            document["text"]
        )

        embeddings.append(
            vector
        )

        metadata.append({

            "table":
                document["table"],

            "text":
                document["text"],

            "foreign_keys":
                document.get(
                    "foreign_keys",
                    []
                )

        })

    result = create_index(
        embeddings,
        metadata
    )

    return {

        "documents":
            len(documents),

        "vectors":
            result["vectors"],

        "dimension":
            result["dimension"]

    }