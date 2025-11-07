from sentence_transformers import SentenceTransformer, util

# Load the embedding model from Hugging Face
model = SentenceTransformer("intfloat/e5-small-v2")

# Example sentences (you can later replace these with lines extracted from a PDF)
sentences = [
    "LangChain is a powerful framework for developing LLM-based applications.",
    "Vector databases store and search high-dimensional embeddings efficiently.",
    "FastAPI and Flask are popular Python frameworks for building APIs.",
    "Google Gemini and OpenAI GPT models can understand and generate human-like text.",
    "Machine learning models require training data for supervised learning."
]

# Create embeddings for each sentence
sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

# Example user query
query = "Which framework helps build LLM apps?"

# Encode the query
query_embedding = model.encode(query, convert_to_tensor=True)

# Compute cosine similarity
similarities = util.cos_sim(query_embedding, sentence_embeddings)[0]

# Find the most similar sentence
best_match_idx = similarities.argmax().item()

print(f"\n🔍 Query: {query}")
print(f"✅ Most relevant sentence: {sentences[best_match_idx]}")
print(f"Similarity score: {similarities[best_match_idx]:.4f}")
