import re

from app.ai.relationship_expander import (
    expand_relationships
)

from app.ai.ollama_client import embed

from app.vectorstore.faiss_store import search


def normalize(value: str):

    value = value.lower()

    value = re.sub(
        r"[^a-z0-9_ ]",
        " ",
        value
    )

    return value


def tokenize(value: str):

    return set(
        normalize(value).split()
    )


def calculate_name_score(
    question: str,
    table_name: str
):

    question_tokens = tokenize(
        question
    )

    table_tokens = tokenize(
        table_name.replace(
            "_",
            " "
        )
    )

    if not question_tokens:
        return 0.0

    matches = (
        question_tokens &
        table_tokens
    )

    return len(matches) / len(
        question_tokens
    )


def search_schema(
    question: str,
    top_k: int = 5
):

    # ============================================
    # 1. CREATE QUESTION EMBEDDING
    # ============================================

    query_embedding = embed(
        question
    )

    # ============================================
    # 2. GET SEMANTIC CANDIDATES
    # ============================================

    semantic_results = search(
        query_embedding,
        max(top_k * 3, 15)
    )

    scored_results = []

    # ============================================
    # 3. SCORE RESULTS
    # ============================================

    for result in semantic_results:

        metadata = result.get(
            "metadata",
            {}
        )

        table_name = metadata.get(
            "table",
            ""
        )

        distance = result.get(
            "distance",
            999
        )

        # FAISS distance:
        # lower = more similar

        semantic_score = 1 / (
            1 + distance
        )

        name_score = calculate_name_score(
            question,
            table_name
        )

        # Stronger weight for exact
        # table-name matching

        final_score = (
            semantic_score * 0.55
            +
            name_score * 0.45
        )

        scored_results.append({

            "score": round(
                final_score,
                6
            ),

            "semantic_distance": distance,

            "name_score": round(
                name_score,
                6
            ),

            "metadata": metadata

        })

    # ============================================
    # 4. SORT BY FINAL SCORE
    # ============================================

    scored_results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # ============================================
    # 5. EXPAND RELATED TABLES
    # ============================================

    expanded_results = expand_relationships(
        scored_results,
        top_k
    )

    return expanded_results