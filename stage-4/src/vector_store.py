"""
vector_store.py

Stage 4: Vector Database Integration

This module provides a VectorStore class that uses ChromaDB to store and retrieve text chunk embeddings.
- Integrates with the EmbeddingModel from Stage 3.
- Supports adding embeddings and similarity search for user queries.
- Designed for educational, incremental development.
"""

import chromadb
from chromadb.config import Settings
import numpy as np

class VectorStore:
    """
    Stores text chunks and their embeddings using ChromaDB.
    Provides similarity search for user queries.
    """
    def __init__(self, collection_name="chatbot_chunks"):
        """
        Initialize the ChromaDB client and collection.
        """
        try:
            self.client = chromadb.Client(Settings())
            self.collection = self.client.get_or_create_collection(collection_name)
        except Exception as e:
            print(f"Error initializing ChromaDB: {e}")
            raise

    def add_embeddings(self, chunks, embeddings):
        """
        Add text chunks and their embeddings to the vector store.
        Args:
            chunks (List[str]): List of text chunks.
            embeddings (np.ndarray): 2D array of embeddings (num_chunks x embedding_dim).
        """
        if not isinstance(chunks, list) or not isinstance(embeddings, np.ndarray):
            raise ValueError("Chunks must be a list of strings and embeddings a numpy array.")
        if len(chunks) != embeddings.shape[0]:
            raise ValueError("Number of chunks and embeddings must match.")
        try:
            # ChromaDB expects embeddings as lists, not numpy arrays
            self.collection.add(
                documents=chunks,
                embeddings=embeddings.tolist(),
                ids=[f"chunk_{i}" for i in range(len(chunks))]
            )
        except Exception as e:
            print(f"Error adding embeddings to ChromaDB: {e}")
            raise

    def query(self, query_text, embedding_model, top_k=3):
        """
        Find the most relevant chunks for a user query.
        Args:
            query_text (str): The user's query.
            embedding_model (EmbeddingModel): The embedding model from Stage 3.
            top_k (int): Number of top results to return.
        Returns:
            List[str]: Most relevant text chunks.
        """
        if not isinstance(query_text, str) or not query_text.strip():
            return []
        try:
            query_embedding = embedding_model.embed_chunks([query_text])[0]
            results = self.collection.query(
                query_embeddings=[query_embedding.tolist()],
                n_results=top_k
            )
            return results.get("documents", [[]])[0]
        except Exception as e:
            print(f"Error querying ChromaDB: {e}")
            return [] 