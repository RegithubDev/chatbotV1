import json
from pathlib import Path

import faiss
import numpy as np


VECTOR_DIRECTORY = Path("data/vectors")

INDEX_FILE = VECTOR_DIRECTORY / "index.faiss"
METADATA_FILE = VECTOR_DIRECTORY / "metadata.json"


def create_index(embeddings, metadata):

    VECTOR_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    vectors = np.array(
        embeddings,
        dtype="float32"
    )

    if len(vectors) == 0:
        raise ValueError("No embeddings provided")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(vectors)

    faiss.write_index(
        index,
        str(INDEX_FILE)
    )

    with open(
        METADATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metadata,
            file,
            indent=2,
            ensure_ascii=False
        )

    return {
        "vectors": len(embeddings),
        "dimension": dimension
    }


def load_index():

    if not INDEX_FILE.exists():
        return None

    return faiss.read_index(
        str(INDEX_FILE)
    )


def load_metadata():

    if not METADATA_FILE.exists():
        return []

    with open(
        METADATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def search(embedding, top_k=5):

    index = load_index()
    metadata = load_metadata()

    if index is None:
        return []

    top_k = min(
        top_k,
        index.ntotal
    )

    vector = np.array(
        [embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        vector,
        top_k
    )

    results = []

    for distance, index_id in zip(
        distances[0],
        indices[0]
    ):

        if index_id < 0:
            continue

        if index_id >= len(metadata):
            continue

        results.append({
            "distance": float(distance),
            "metadata": metadata[index_id]
        })

    return results