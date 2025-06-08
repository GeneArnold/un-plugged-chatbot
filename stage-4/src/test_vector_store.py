"""
test_vector_store.py

Test script for Stage 4 VectorStore.
Demonstrates adding embeddings and querying for relevant chunks.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../stage-3/src')))
from embedding_model import EmbeddingModel
from vector_store import VectorStore

if __name__ == "__main__":
    # Sample text chunks
    chunks = [
        "The quick brown fox jumps over the lazy dog.",
        "A chatbot can use embeddings to find relevant information.",
        "Embeddings are numerical representations of text.",
        "Install the software by running the setup script.",
        "For help, consult the user manual or support page.",
        "You should read the manual to repair you mountain bike"
    ]

    # Initialize the embedding model (from Stage 3)
    model = EmbeddingModel()
    print("Embedding model loaded.")

    # Generate embeddings
    embeddings = model.embed_chunks(chunks)
    print(f"Embeddings shape: {embeddings.shape}")

    # Initialize the vector store
    store = VectorStore()
    print("Vector store initialized.")

    # Add embeddings to the store
    store.add_embeddings(chunks, embeddings)
    print("Embeddings added.")

    # Query the store
    # query = "How do I install the software?"
    query = "How do I fix my mountain bike?"
    results = store.query(query, model, top_k=2)
    print(f"Query: {query}")
    print(f"Top results: {results}") 