import requests
from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer("all-MiniLM-L6-v2")
ENDEE_URL = "http://localhost:8080/api/v1/index/documents"
INDEX_NAME = "documents"

headers = {"Content-Type": "application/json"}

for file in os.listdir("data/documents"):
    text = open(f"data/documents/{file}").read()
    vector = model.encode(text).tolist()

    payload = {
        "index": INDEX_NAME,
        "id": file,
        "vector": vector,
        "metadata": {"text": text}
    }

    r = requests.post(ENDEE_URL, json=payload, headers=headers)
    print(file, r.status_code)