"""
test_embedding.py

Test script for Stage 3 EmbeddingModel.
Demonstrates loading the model and generating embeddings for sample text chunks.
"""
from embedding_model import EmbeddingModel

if __name__ == "__main__":
    # Sample text chunks
    chunks = [
        "The quick brown fox jumps over the lazy dog.",
        "A chatbot can use embeddings to find relevant information.",
        "Embeddings are numerical representations of text."
    ]

    # Initialize the embedding model
    model = EmbeddingModel()
    print("Model loaded.")

    # Generate embeddings
    embeddings = model.embed_chunks(chunks)
    print(f"Embeddings shape: {embeddings.shape}")
    print(f"First embedding (truncated): {embeddings[0][:8]} ...") 