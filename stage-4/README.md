# Stage 4: Vector Database Integration

**Building an Offline LLM Chatbot - Educational Series**

Welcome to Stage 4! This stage adds persistent, efficient storage and retrieval of embeddings using a vector database (ChromaDB). You'll learn how to store, search, and retrieve relevant document chunks for user queries, completing the retrieval part of RAG.

## 🎯 Learning Objectives

By completing Stage 4, you will:

- ✅ Understand what a vector database is and why it's needed for RAG
- ✅ Use ChromaDB to store and search embeddings
- ✅ Integrate vector storage with your embedding pipeline
- ✅ Test and verify similarity search and retrieval
- ✅ Extend the architecture cleanly (building on Stage 3)

## 🏗️ What We're Building

Stage 4 introduces a `VectorStore` class and supporting scripts:

1. **Vector Database Integration** - Store and retrieve embeddings with ChromaDB
2. **Similarity Search** - Find relevant chunks for user queries
3. **Testing** - Verify storage and retrieval with dedicated scripts
4. **Educational Documentation** - Clear, incremental learning journey

## 📋 Prerequisites

- **Stage 3 completed** - This builds directly on Stage 3's foundation
- Python 3.11 or higher
- Basic understanding of embeddings

## 🚀 Quick Start

### 1. Set Up Your Environment

```bash
# Create and activate virtual environment (if not already done)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (includes ChromaDB)
pip install -e .
```

### 2. Test Vector Storage and Search

```bash
# Run the vector store test script
python src/test_vector_store.py
```

### 3. Expected Output

When you run `python src/test_vector_store.py`:

```
Vector store initialized.
Embeddings added.
Query: ...
Top result: ...
```

## 📁 Project Structure

```
stage-4/
├── src/
│   ├── vector_store.py         # Vector database logic
│   ├── test_vector_store.py    # Test script
│   └── ...
├── sample_documents/          # Example documents (from previous stages)
├── main.py                    # CLI interface
├── README.md                  # This file
└── ...
```

## 🔍 Key Components Explained

### VectorStore Class

All Stage 3 functionality remains unchanged, plus new vector storage methods:

```python
# All Stage 3 capabilities still work
from embedding_model import EmbeddingModel
model = EmbeddingModel()
embeddings = model.embed_chunks(chunks)

# NEW Stage 4 capabilities
from vector_store import VectorStore
store = VectorStore()
store.add_embeddings(chunks, embeddings)
results = store.query("How do I install the software?")
```

### Vector Database Pipeline

```python
def add_embeddings(self, chunks: List[str], embeddings: np.ndarray):
    """
    Store text chunks and their embeddings in ChromaDB.
    """

def query(self, query_text: str) -> List[str]:
    """
    Find and return the most relevant chunks for a query.
    """
```

## 🧪 Enhanced Testing

Stage 4 adds comprehensive vector store tests:

```bash
python src/test_vector_store.py

# Tests now include:
# ✅ Vector store initializes and persists
# ✅ Embeddings are added and retrievable
# ✅ Similarity search returns relevant chunks
# ✅ Handles empty/invalid queries gracefully
```

## 🛠️ New Dependencies

Stage 4 adds vector database libraries:

- **chromadb** - Persistent, efficient vector storage and search

```bash
# Install automatically with:
pip install -e .
```

## 💡 Key Learning Points

### 1. Extending vs. Replacing
Notice how we **extended** Stage 3 rather than replacing it:
- All Stage 3 functionality works exactly as before
- New features are added as additional modules
- Configuration grows without breaking existing settings

### 2. What Is a Vector Database?
A vector database stores high-dimensional vectors (embeddings) and enables fast similarity search, which is essential for RAG systems.

### 3. How Vector Search Fits the Pipeline
- Embeddings from Stage 3 are stored in ChromaDB
- User queries are embedded and compared to stored vectors
- Most similar chunks are retrieved for LLM context

## 🔮 What's Next: Stage 5 Preview

Stage 5 will add **local LLM integration** to your chatbot:

```python
# Stage 5 will add LLM inference
response = chatbot.answer_query("How do I install the software?")
```

Key concepts in Stage 5:
- Running a local LLM (e.g., llama.cpp)
- Integrating retrieval and generation
- Building a full RAG pipeline

## 🛠️ Troubleshooting

### Common Issues

**"No module named 'chromadb'"**
```bash
# Reinstall dependencies
pip install -e .
```

**"Vector store fails to initialize"**
- Check your Python version and dependencies
- Ensure correct file paths and permissions

### Getting Help

- Check `python src/test_vector_store.py` output for detailed error information
- Verify all Stage 3 functionality works first
- Ensure you're in the `stage-4/` directory when running commands

## 🎓 Educational Notes

### Key Architectural Decisions

1. **Incremental Enhancement**: We extended rather than replaced Stage 3
2. **Separation of Concerns**: Vector storage logic is isolated in its own module
3. **Comprehensive Testing**: Each new feature has corresponding tests
4. **User Experience**: Clear error messages and educational output

### Real-World Applications

The vector store we're building forms the foundation for:
- **Semantic Search Engines**: Find relevant information by meaning
- **Knowledge Bases**: Power corporate or personal document search
- **AI Assistants**: Enable context-aware responses

## 📚 Additional Resources

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Vector Database Concepts](https://www.pinecone.io/learn/vector-database/)

## ✅ Stage 4 Checklist

Before moving to Stage 5, verify:

- [ ] All Stage 3 functionality still works (`python main.py --status`)
- [ ] Can process, chunk, and embed documents (`python main.py --demo-docs`)
- [ ] Vector store test script works (`python src/test_vector_store.py`)
- [ ] All tests pass (`python main.py --test`)
- [ ] Understand how vector storage and search work
- [ ] Ready to integrate a local LLM in Stage 5

## 🎯 Try It Yourself

### Experiment with Your Own Queries

1. Modify `test_vector_store.py` to use your own queries
2. Run the script and observe the results
3. Try different queries and see how retrieval changes

**Ready for Stage 5?** The next stage will add local LLM integration to your chatbot!

---

*This is part of the "Building an Offline LLM Chatbot" educational series. Stage 4 builds directly on Stage 3's foundation, demonstrating how to grow complex systems incrementally.* 