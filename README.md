Semantic Search using Endee Vector Database
📖 Project Overview

This project implements a Semantic Search system using Endee as the vector database.
Text documents are converted into vector embeddings and stored in Endee.
When a user submits a query, it is embedded and matched against stored vectors using similarity search to retrieve the most relevant documents.

The project demonstrates a real-world use case of vector databases for intelligent information retrieval.

🚀 Key Features

Semantic search based on meaning, not keywords

Vector storage and retrieval using Endee

Sentence embeddings using SentenceTransformers

REST-based communication with the vector database

Modular and easy-to-extend design

🧠 Use Case

This system can be used for:

Document search engines

Knowledge base search

Resume / article / note retrieval

Foundation for RAG (Retrieval Augmented Generation) pipelines

Vector search is the core component of this project.

🛠️ Tech Stack

Python

Endee (Vector Database)

SentenceTransformers

REST APIs

Docker (for running Endee)

📂 Project Structure
endee-semantic-search/
├── data/                  # Sample documents
├── src/
│   ├── insert_vectors.py  # Inserts document vectors into Endee
│   ├── search.py          # Performs semantic search queries
│   └── config.py          # Configuration (Endee URL, index name)
├── screenshots/           # Output screenshots (optional)
├── requirements.txt
├── README.md
└── .gitignore

🔗 Dependency: Endee Vector Database

This project uses Endee as the vector database.

You must fork and run Endee separately.

Endee Repository:
👉 https://github.com/EndeeLabs/endee

⚙️ Setup Instructions
1️⃣ Clone and Run Endee
git clone https://github.com/<your-username>/endee
cd endee
docker-compose up


Endee will start at:

http://localhost:8080

2️⃣ Clone This Project
git clone https://github.com/<your-username>/endee-semantic-search
cd endee-semantic-search

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run the Project
Step 1: Insert Documents into Endee
python src/insert_vectors.py


This:

Reads documents

Converts them into embeddings

Stores vectors in Endee

Step 2: Perform Semantic Search
python src/search.py


Enter a query and the system will return the most semantically similar documents.

📊 Example Output
User Query: "AI projects using vector databases"

Top Results:
1. Document ID: 3 | Similarity Score: 0.92
2. Document ID: 7 | Similarity Score: 0.88
3. Document ID: 1 | Similarity Score: 0.84

🧩 How It Works (Architecture)
User Query
   ↓
Sentence Transformer Embedding
   ↓
Vector Similarity Search (Endee)
   ↓
Top-K Relevant Documents

This architecture ensures fast and accurate semantic retrieval.

🔮 Future Enhancements

Add Retrieval Augmented Generation (RAG) with an LLM

Web UI for search

Metadata-based filtering

Scalability testing with large datasets

✅ Evaluation Criteria Mapping
Requirement	Status
Use of Endee	✅
Vector Search Core	✅
Practical AI Use Case	✅
GitHub Hosted Project	✅
Clean README	✅
📜 License

This project is for educational and evaluation purposes.
