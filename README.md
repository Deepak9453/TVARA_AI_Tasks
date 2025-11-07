🚀 Task B — API Integration (Gemini 2.0 Flash)
🎯 Goal

Build a simple backend (Flask API) that:

Accepts a user prompt.

Sends it to Google Gemini 2.0 Flash API.

Returns the generated response neatly (optionally with raw debug output).

🧩 Technologies Used

Flask (for REST API)

Requests (for HTTP calls)

Google Gemini 2.0 Flash API

🧠 Implementation Summary

The /generate endpoint:

Accepts a prompt (via GET or POST).

Sends the request to the Gemini API endpoint:

https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent


Returns a clean JSON response or full raw data if debug=true.

⚙️ How to Run
pip install flask requests
python task2_gemini_api.py

🧪 Example Usage

Browser / Curl:

http://127.0.0.1:5000/generate?prompt=Explain+LangChain


POST (JSON):

{
  "prompt": "Explain Retrieval-Augmented Generation",
  "debug": true
}


✅ Example Response:

{
  "response": "LangChain is a framework designed to build applications powered by large language models..."
}


🔐 Note: Replace the demo API key with your own from Google AI Studio
 for live testing.

🧮 Task C — Vectorization with Hugging Face
🎯 Goal

Demonstrate text vectorization and similarity search using the intfloat/e5-small-v2 embedding model.

🧩 Technologies Used

sentence-transformers

Hugging Face Model Hub

PyTorch

🧠 Implementation Summary

Load model intfloat/e5-small-v2 using SentenceTransformers.

Embed a set of example sentences.

Given a query, compute cosine similarity.

Return the most semantically similar sentence.

⚙️ How to Run
pip install sentence-transformers torch
python task3_vectorization.py

🧪 Example Output
🔍 Query: Which framework helps build LLM apps?
✅ Most relevant sentence: LangChain is a powerful framework for developing LLM-based applications.
Similarity score: 0.8234

🧰 Skills Demonstrated

LLM API Integration (Gemini)

RESTful Backend Development (Flask)

Embedding & Vectorization Concepts

Semantic Search using Cosine Similarity

Python Coding Best Practices

👨‍💻 Author

Deepak Kumar Prajapati
B.Tech CSE (AI) | AI & Data Science Enthusiast
📍 Chhatrapati Shahu Ji Maharaj University, Kanpur
🔗 LinkedIn

📧 deepakkumarprajapati256@gmail.com
