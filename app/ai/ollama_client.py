import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://127.0.0.1:11434"
)

GENERATION_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5-coder:7b-instruct"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "nomic-embed-text:latest"
)


def generate(
    prompt: str,
    timeout: int = 45,
    num_predict: int = 60,
    num_ctx: int = 1024
):

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": GENERATION_MODEL,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "10m",
            "options": {
                "temperature": 0,
                "num_predict": num_predict,
                "num_ctx": num_ctx
            }
        },
        timeout=timeout
    )

    response.raise_for_status()

    data = response.json()

    result = data.get(
        "response",
        ""
    ).strip()

    if not result:
        raise RuntimeError(
            "Ollama returned an empty response"
        )

    return result


def embed(text: str):

    response = requests.post(
        f"{OLLAMA_URL}/api/embed",
        json={
            "model": EMBEDDING_MODEL,
            "input": text
        },
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    embeddings = data.get(
        "embeddings"
    )

    if not embeddings:
        raise RuntimeError(
            "Ollama returned no embeddings"
        )

    return embeddings[0]
