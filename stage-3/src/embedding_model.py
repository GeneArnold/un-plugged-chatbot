"""
embedding_model.py

Stage 3: Embeddings

This module will provide functionality to load a sentence-transformers embedding model (all-MiniLM-L6-v2) and generate embeddings for text chunks.

- Uses HuggingFace sentence-transformers and torch.
- Designed for educational, incremental development.
"""

# Placeholder for imports
# from sentence_transformers import SentenceTransformer
# import torch

from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingModel:
    """
    Loads the embedding model and provides a method to generate embeddings for a list of text chunks.
    """
    def __init__(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'):
        """
        Initialize the embedding model. Downloads the model if not present.
        """
        try:
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            print(f"Error loading embedding model: {e}")
            raise

    def embed_chunks(self, chunks):
        """
        Given a list of text chunks, return their embeddings as numpy arrays.
        Args:
            chunks (List[str]): List of text strings to embed.
        Returns:
            np.ndarray: 2D array of embeddings (num_chunks x embedding_dim)
        """
        if not isinstance(chunks, list) or not all(isinstance(c, str) for c in chunks):
            raise ValueError("Input to embed_chunks must be a list of strings.")
        try:
            embeddings = self.model.encode(chunks, show_progress_bar=False, convert_to_numpy=True)
            return embeddings
        except Exception as e:
            print(f"Error generating embeddings: {e}")
            raise 