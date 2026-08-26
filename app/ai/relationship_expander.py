def expand_relationships(
    search_results,
    top_k=8
):

    selected = []

    selected_tables = set()

    # ------------------------------------------------
    # 1. Select strongest semantic candidates
    # ------------------------------------------------

    for result in search_results:

        metadata = result.get(
            "metadata",
            {}
        )

        table_name = metadata.get(
            "table"
        )

        if not table_name:
            continue

        key = table_name.lower()

        if key in selected_tables:
            continue

        selected.append(
            result
        )

        selected_tables.add(
            key
        )

        if len(selected) >= top_k:
            break

    # ------------------------------------------------
    # 2. Build relationship graph from ALL
    #    FAISS candidates available
    # ------------------------------------------------

    graph = {}

    for result in search_results:

        metadata = result.get(
            "metadata",
            {}
        )

        table_name = metadata.get(
            "table"
        )

        if not table_name:
            continue

        table_key = table_name.lower()

        graph.setdefault(
            table_key,
            set()
        )

        for fk in metadata.get(
            "foreign_keys",
            []
        ):

            referred = fk.get(
                "referred_table"
            )

            if referred:

                referred_key = (
                    referred.lower()
                )

                graph[
                    table_key
                ].add(
                    referred_key
                )

                graph.setdefault(
                    referred_key,
                    set()
                ).add(
                    table_key
                )

    # ------------------------------------------------
    # 3. Expand one relationship hop
    # ------------------------------------------------

    related_tables = set()

    for table in list(
        selected_tables
    ):

        related_tables.update(
            graph.get(
                table,
                set()
            )
        )

    # ------------------------------------------------
    # 4. Add related candidates
    # ------------------------------------------------

    for result in search_results:

        metadata = result.get(
            "metadata",
            {}
        )

        table_name = metadata.get(
            "table"
        )

        if not table_name:
            continue

        table_key = table_name.lower()

        if (
            table_key in related_tables
            and
            table_key not in selected_tables
        ):

            selected.append(
                result
            )

            selected_tables.add(
                table_key
            )

    return selected
