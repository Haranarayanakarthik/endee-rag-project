from sentence_transformers import SentenceTransformer
import requests
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

ENDEE_URL = "http://localhost:8080/api/v1/index/documents/search"

# Local fallback corpus
LOCAL_DOCS = [
    "Endee is a high-performance open source vector database optimized for fast semantic search using SIMD instructions."
]

def semantic_search(query: str, k: int = 3):
    vector = model.encode(query).tolist()

    # Try Endee first
    try:
        payload = {"vector": vector, "k": k}
        r = requests.post(ENDEE_URL, json=payload, timeout=2)

        if r.status_code == 200:
            data = r.json()
            results = data.get("results", []) or data.get("matches", [])
            if results:
                return results
    except Exception:
        pass  # Endee fallback

    # 🔁 Fallback: local semantic match
    q_vec = model.encode(query)
    scores = []

    for text in LOCAL_DOCS:
        d_vec = model.encode(text)
        score = (q_vec @ d_vec) / (
            (q_vec @ q_vec) ** 0.5 * (d_vec @ d_vec) ** 0.5
        )
        scores.append((score, text))

    scores.sort(reverse=True)
    return [
        {"metadata": {"text": scores[0][1]}}
    ]
