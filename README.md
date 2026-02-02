📌 Semantic Search System using Endee Vector Database
1. Project Overview

Modern search systems often fail to understand the meaning of user queries and rely only on keyword matching. This leads to irrelevant results when different words express similar intent.

This project implements a Semantic Search system that retrieves documents based on context and meaning, rather than exact keywords. It uses Endee as the vector database to store and search embeddings generated from text documents.

2. Problem Statement

Traditional keyword-based search systems:

Fail to capture semantic meaning

Return poor results for natural language queries

Do not scale well for intelligent retrieval systems

Objective:
To build a practical AI system that uses vector similarity search to retrieve the most relevant documents based on user intent.

3. System Design / Technical Approach
High-Level Architecture
User Query
   ↓
Text Embedding (SentenceTransformers)
   ↓
Vector Similarity Search (Endee)
   ↓
Top-K Relevant Documents

Technical Workflow

Input documents are converted into dense vector embeddings

Vectors are stored in Endee along with metadata

User queries are embedded using the same model

Endee performs similarity search using vector distance

Most relevant documents are returned

Vector search is the core mechanism of this system.

4. Explanation of How Endee Is Used

Endee is used as the vector database in this project.

Role of Endee:

Stores high-dimensional vector embeddings

Performs fast similarity search

Exposes a REST API for vector operations

How the Project Interacts with Endee:

Document vectors are inserted into Endee via API calls

Query vectors are sent to Endee for similarity search

Endee returns top-K matching vectors

Endee runs as a separate service, and the project communicates with it over HTTP.

5. Tech Stack

Python

Endee (Vector Database)

SentenceTransformers

REST APIs

Docker

6. Project Structure
endee-semantic-search/
├── data/                  # Sample input documents
├── src/
│   ├── insert_vectors.py  # Inserts vectors into Endee
│   ├── search.py          # Performs semantic search
│   └── config.py          # Endee configuration
├── screenshots/           # Output screenshots (optional)
├── requirements.txt
├── README.md
└── .gitignore

7. Setup Instructions
Step 1: Fork and Run Endee
git clone https://github.com/<your-username>/endee
cd endee
docker-compose up


Endee will be available at:

http://localhost:8080

Step 2: Clone This Project
git clone https://github.com/<your-username>/endee-semantic-search
cd endee-semantic-search

Step 3: Install Dependencies
pip install -r requirements.txt

8. Execution Instructions
Insert Document Vectors
python src/insert_vectors.py


This step:

Reads documents

Converts them to embeddings

Stores them in Endee

Perform Semantic Search
python src/search.py


9. Conclusion

This project demonstrates a real-world semantic search application using Endee as a vector database. It highlights how vector embeddings and similarity search can be used to build intelligent retrieval systems and serves as a strong foundation for future RAG-based applications.


Output from my device:
<img width="985" height="580" alt="image" src="https://github.com/user-attachments/assets/0040137f-84d9-4309-a2ea-e4af5da4efc5" />

<img width="1500" height="677" alt="image" src="https://github.com/user-attachments/assets/d9e333d5-ae8a-4a2d-b768-dbb852bc2cf0" />
