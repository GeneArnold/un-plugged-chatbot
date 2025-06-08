# Stage 3: Embeddings

**Building an Offline LLM Chatbot - Educational Series**

Welcome to Stage 3! This stage builds on our document processing foundation by adding semantic understanding through vector embeddings. You'll learn how to convert text chunks into numerical vectors using state-of-the-art models, setting the stage for similarity search and retrieval in future stages.

## 🎯 Learning Objectives

By completing Stage 3, you will:

- ✅ Understand what embeddings are and why they're essential for RAG
- ✅ Use HuggingFace sentence-transformers to generate embeddings
- ✅ Integrate embeddings into your document processing pipeline
- ✅ Test and verify embedding generation
- ✅ Extend the architecture cleanly (building on Stage 2)

## 🏗️ What We're Building

Stage 3 introduces an `EmbeddingModel` class and supporting scripts:

1. **Text Embedding** - Convert document chunks into 384-dimensional vectors
2. **Model Integration** - Use all-MiniLM-L6-v2 via sentence-transformers
3. **Testing** - Verify embeddings with a dedicated script
4. **Educational Documentation** - Clear, incremental learning journey

## 📋 Prerequisites

- **Stage 2 completed** - This builds directly on Stage 2's foundation
- Python 3.11 or higher
- Basic understanding of document chunking

## 🚀 Quick Start

### 1. Set Up Your Environment

```bash
# Create and activate virtual environment (if not already done)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (includes new embedding libraries)
pip install -e .
```

### 2. Test Embedding Generation

```bash
# Run the embedding test script
python src/test_embedding.py
```

### 3. Expected Output

When you run `python src/test_embedding.py`:

```
Model loaded.
Embeddings shape: (3, 384)
First embedding (truncated): [ ... ] ...
```

## 📁 Project Structure

```
stage-3/
├── src/
│   ├── embedding_model.py      # Embedding logic
│   ├── test_embedding.py       # Test script
│   └── ...
├── sample_documents/          # Example documents (from Stage 2)
├── main.py                    # CLI interface
├── README.md                  # This file
└── ...
```

## 🔍 Key Components Explained

### EmbeddingModel Class

All Stage 2 functionality remains unchanged, plus new embedding methods:

```python
# All Stage 2 capabilities still work
chatbot = ChatbotCore()
chunks = chatbot.process_document("manual.pdf")

# NEW Stage 3 capabilities
from embedding_model import EmbeddingModel
model = EmbeddingModel()
embeddings = model.embed_chunks(chunks)
```

### Embedding Generation Pipeline

```python
def embed_chunks(self, chunks: List[str]) -> np.ndarray:
    """
    Convert a list of text chunks into embeddings using all-MiniLM-L6-v2.
    Returns: 2D numpy array (num_chunks x 384)
    """
```

## 🧪 Enhanced Testing

Stage 3 adds comprehensive embedding tests:

```bash
python src/test_embedding.py

# Tests now include:
# ✅ Model loads without error
# ✅ Embeddings generated for sample chunks
# ✅ Handles invalid input gracefully
```

## 🛠️ New Dependencies

Stage 3 adds embedding libraries:

- **sentence-transformers** - Easy access to HuggingFace models
- **torch** - Backend for model computation

```bash
# Install automatically with:
pip install -e .
```

## 💡 Key Learning Points

### 1. Extending vs. Replacing
Notice how we **extended** Stage 2 rather than replacing it:
- All Stage 2 functionality works exactly as before
- New features are added as additional modules
- Configuration grows without breaking existing settings

### 2. What Are Embeddings?
Embeddings are numerical representations of text that capture semantic meaning, enabling similarity search and retrieval in RAG systems.

### 3. Model Choice
- **all-MiniLM-L6-v2**: Lightweight, fast, and effective for sentence/paragraph embeddings
- **sentence-transformers**: Easy-to-use wrapper for HuggingFace models
- **torch**: Backend for model computation

### 4. How Embeddings Fit the Pipeline
- Chunks from Stage 2 are passed to the embedding model
- Embeddings are generated and can be stored or searched in later stages

## 🔮 What's Next: Stage 4 Preview

Stage 4 will add **vector storage and similarity search** to your chatbot:

```python
# Stage 4 will add vector database integration
results = chatbot.find_similar_chunks(query="How do I install the software?", chunks=processed_chunks)
```

Key concepts in Stage 4:
- Vector databases and efficient search
- Storing and retrieving embeddings
- Integrating retrieval with the chatbot pipeline

## 🛠️ Troubleshooting

### Common Issues

**"No module named 'sentence_transformers'"**
```bash
# Reinstall dependencies
pip install -e .
```

**"Model fails to load"**
- Check your internet connection (model downloads on first run)
- Ensure correct Python version and dependencies

### Getting Help

- Check `python src/test_embedding.py` output for detailed error information
- Verify all Stage 2 functionality works first
- Ensure you're in the `stage-3/` directory when running commands

## 🎓 Educational Notes

### Key Architectural Decisions

1. **Incremental Enhancement**: We extended rather than replaced Stage 2
2. **Separation of Concerns**: Embedding logic is isolated in its own module
3. **Comprehensive Testing**: Each new feature has corresponding tests
4. **User Experience**: Clear error messages and educational output

### Real-World Applications

The embedding system we're building forms the foundation for:
- **Semantic Search Engines**: Find relevant information by meaning
- **Knowledge Bases**: Power corporate or personal document search
- **AI Assistants**: Enable context-aware responses

## 📚 Additional Resources

- [Sentence Transformers Documentation](https://www.sbert.net/)
- [HuggingFace Model Hub](https://huggingface.co/models)
- [Understanding Embeddings](https://jalammar.github.io/illustrated-word2vec/)

## ✅ Stage 3 Checklist

Before moving to Stage 4, verify:

- [ ] All Stage 2 functionality still works (`python main.py --status`)
- [ ] Can process and chunk documents (`python main.py --demo-docs`)
- [ ] Embedding test script works (`python src/test_embedding.py`)
- [ ] All tests pass (`python main.py --test`)
- [ ] Understand how embeddings are generated and used
- [ ] Ready to store and search embeddings in Stage 4

## 🎯 Try It Yourself

### Experiment with Your Own Text

1. Modify `test_embedding.py` to use your own text chunks
2. Run the script and observe the embeddings
3. Try different sentences and see how the vectors change

**Ready for Stage 4?** The next stage will add vector storage and similarity search to your chatbot!

---

*This is part of the "Building an Offline LLM Chatbot" educational series. Stage 3 builds directly on Stage 2's foundation, demonstrating how to grow complex systems incrementally.* 