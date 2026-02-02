from fastapi import FastAPI
from pydantic import BaseModel
from backend.search import semantic_search
from backend.rag import generate_answer

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def health():
    return {"status": "API running"}

@app.post("/search")
def search(req: QueryRequest):
    docs = semantic_search(req.query)
    answer = generate_answer(req.query, docs)

    return {
        "query": req.query,
        "answer": answer,
        "documents": docs
    }
