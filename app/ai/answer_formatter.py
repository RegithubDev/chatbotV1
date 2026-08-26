def format_answer(
    question: str,
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

    columns = result.get(
        "columns",
        []
    )

    question_lower = question.lower()

    # =========================================================
    # EMPTY RESULT
    # =========================================================

    if row_count == 0:

        return {
            "text": "No matching records were found.",
            "row_count": 0
        }

    # =========================================================
    # COUNT QUESTIONS
    # =========================================================

    if (
        "how many" in question_lower
        or "count" in question_lower
        or "number of" in question_lower
    ):

        if (
            len(rows) == 1
            and len(columns) == 1
        ):

            value = rows[0].get(
                columns[0]
            )

            return {
                "text": f"The result is {value}.",
                "row_count": row_count
            }

    # =========================================================
    # FIRST / TOP / N RECORDS
    # =========================================================

    if (
        "first" in question_lower
        or "top" in question_lower
        or "records" in question_lower
        or "show" in question_lower
        or "list" in question_lower
    ):

        return {
            "text": (
                f"Here are the {row_count} "
                f"matching records."
            ),
            "row_count": row_count
        }

    # =========================================================
    # DEFAULT
    # =========================================================

    return {
        "text": (
            f"Found {row_count} matching "
            f"record(s)."
        ),
        "row_count": row_count
    }
