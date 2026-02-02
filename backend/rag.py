def generate_answer(query, docs):
    if not docs:
        return "No answer found."

    context = docs[0]["metadata"]["text"]
    return f"{context}"
