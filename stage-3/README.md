# Stage 2: Document Processing

**Building an Offline LLM Chatbot - Educational Series**

Welcome to Stage 2! This stage builds on our Stage 1 foundation by adding comprehensive document processing capabilities. We'll learn how to extract text from various file formats and prepare them for AI processing.

## 🎯 Learning Objectives

By completing Stage 2, you will:

- ✅ Extract text from PDF, TXT, Markdown, and DOCX files
- ✅ Implement intelligent text chunking with overlap strategies
- ✅ Build file processing pipelines for batch operations
- ✅ Understand document metadata and processing workflows
- ✅ Create sample documents for testing and experimentation
- ✅ Extend existing architecture cleanly (building on Stage 1)

## 🏗️ What We're Building

Stage 2 extends our `ChatbotCore` class with document processing:

1. **Multi-Format Text Extraction** - PDF, TXT, Markdown, DOCX support
2. **Smart Text Chunking** - Configurable chunk size with overlap
3. **Batch Processing** - Handle multiple documents efficiently
4. **Sample Document Generator** - Create test files for experimentation
5. **Enhanced Testing** - Document-specific test coverage
6. **Beautiful Progress Reporting** - Rich console output for processing status

## 📋 Prerequisites

- **Stage 1 completed** - This builds directly on Stage 1's foundation
- Python 3.11 or higher
- Basic understanding of file processing concepts

## 🚀 Quick Start

### 1. Set Up Your Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (includes new document processing libraries)
pip install -e .
```

### 2. Test Document Processing

```bash
# Create sample documents for testing
python main.py --create-samples

# See document processing in action
python main.py --demo-docs

# Run all system tests (includes new document tests)
python main.py --test

# Check enhanced system status
python main.py --status
```

### 3. Expected Output

When you run `python main.py --demo-docs`:

```
🔧 Document Processing Demo

Processing document: technical_guide.md
✅ Processed technical_guide.md: 1 chunks, 905 characters
   📄 Created 1 chunks from technical_guide.md
   📝 Preview: # Technical Setup Guide...

Processing document: company_policy.txt
✅ Processed company_policy.txt: 1 chunks, 812 characters
   📄 Created 1 chunks from company_policy.txt
   📝 Preview: Company Employee Handbook...

📊 Processing Summary:
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Metric           ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Total Documents  │ 3     │
│ Total Chunks     │ 3     │
│ Total Characters │ 2,487 │
└──────────────────┴───────┘
```

## 📁 Project Structure

```
stage-2/
├── src/
│   ├── __init__.py          # Package initialization
│   └── chatbot_core.py      # Extended ChatbotCore class
├── sample_documents/        # NEW: Generated test documents
│   ├── company_policy.txt
│   ├── technical_guide.md
│   └── meeting_notes.txt
├── main.py                  # Enhanced demo script with new commands
├── pyproject.toml          # Updated dependencies
└── README.md               # This file
```

## 🔍 Key Components Explained

### Enhanced ChatbotCore Class

All Stage 1 functionality remains unchanged, plus new document processing methods:

```python
# All Stage 1 capabilities still work
chatbot = ChatbotCore()
chatbot.initialize()
print(chatbot.get_capabilities())
# Output: ['basic_setup', 'configuration', 'logging', 'document_processing', 'text_chunking']

# NEW Stage 2 capabilities
chunks = chatbot.process_document("manual.pdf")
formats = chatbot.get_supported_formats()
chatbot.create_sample_documents()
```

### Document Processing Pipeline

```python
def process_document(self, file_path: str) -> List[str]:
    """
    Extract text from a document and split into chunks.
    
    Supports: .pdf, .txt, .md, .markdown, .docx
    Returns: List of text chunks with smart overlap
    """
```

### Text Chunking Strategy

```python
def _chunk_text(self, text: str) -> List[str]:
    """
    Split text into overlapping chunks.
    
    Default: 1000 characters per chunk, 200 character overlap
    Overlap preserves context across chunk boundaries
    """
```

## 🧪 Enhanced Testing

Stage 2 adds comprehensive document processing tests:

```bash
python main.py --test

# Tests now include:
# ✅ All Stage 1 tests (unchanged)
# ✅ Document format support verification
# ✅ Text extraction accuracy
# ✅ Chunking logic validation
# ✅ Sample document generation
# ✅ Error handling for invalid files
```

## 🛠️ New Dependencies

Stage 2 adds document processing libraries:

- **PyPDF** - PDF text extraction
- **python-docx** - Microsoft Word document support
- **markdown** - Markdown processing (for future enhancements)

```bash
# Install automatically with:
pip install -e .
```

## 💡 Key Learning Points

### 1. Extending vs. Replacing
Notice how we **extended** Stage 1 rather than replacing it:
- All Stage 1 functionality works exactly as before
- New features are added as additional methods
- Configuration grows without breaking existing settings

### 2. File Format Strategies
Different formats require different extraction approaches:
- **TXT/MD**: Simple file reading
- **PDF**: PyPDF library for page-by-page extraction
- **DOCX**: python-docx for structured paragraph extraction

### 3. Chunking for AI Systems
Why we chunk text:
- **LLM Context Limits**: Models have maximum input lengths
- **Semantic Coherence**: Smaller chunks = more focused retrieval
- **Processing Efficiency**: Faster embedding and search operations

### 4. Overlap Strategy
Chunk overlap preserves context across boundaries:
```
Chunk 1: [----1000 chars----]
Chunk 2:      [200 overlap][----800 new chars----]
Chunk 3:                           [200 overlap][----800 new chars----]
```

## 🔮 What's Next: Stage 3 Preview

Stage 3 will add **semantic understanding** to our processed text chunks:

```python
# Stage 3 will add embeddings
similarity = chatbot.find_similar_chunks(
    query="How do I install the software?",
    chunks=processed_chunks
)
```

Key concepts in Stage 3:
- Vector embeddings and semantic similarity
- Sentence transformer models
- Cosine similarity calculations
- Preparing for vector database storage

## 🛠️ Troubleshooting

### Common Issues

**"No module named 'pypdf'"**
```bash
# Reinstall dependencies
pip install -e .
```

**"Failed to process PDF"**
- Some PDFs are image-based and need OCR (beyond this tutorial)
- Try with text-based PDFs first

**"Sample documents not created"**
```bash
# Check write permissions in current directory
ls -la sample_documents/
```

### Getting Help

- Check `python main.py --test` output for detailed error information
- Verify all Stage 1 functionality works first
- Ensure you're in the `stage-2/` directory when running commands

## 🎓 Educational Notes

### Key Architectural Decisions

1. **Incremental Enhancement**: We extended rather than replaced Stage 1
2. **Flexible Configuration**: Document settings added to existing config system
3. **Comprehensive Testing**: Each new feature has corresponding tests
4. **User Experience**: Beautiful progress reporting and error handling

### Real-World Applications

The document processing we're building forms the foundation for:
- **Corporate Knowledge Bases**: Process company documents
- **Technical Documentation Systems**: Handle manuals and guides
- **Research Tools**: Analyze academic papers and reports
- **Personal AI Assistants**: Process your own document collections

## 📚 Additional Resources

- [PyPDF Documentation](https://pypdf.readthedocs.io/) - PDF processing
- [python-docx Documentation](https://python-docx.readthedocs.io/) - Word document handling
- [Text Chunking Strategies](https://chunkviz.up.railway.app/) - Visualization tool

## ✅ Stage 2 Checklist

Before moving to Stage 3, verify:

- [ ] All Stage 1 functionality still works (`python main.py --status`)
- [ ] Can create sample documents (`python main.py --create-samples`)
- [ ] Document processing demo works (`python main.py --demo-docs`)
- [ ] All tests pass (`python main.py --test`)
- [ ] Understand text chunking concepts
- [ ] Can process your own documents by adding them to `sample_documents/`

## 🎯 Try It Yourself

### Experiment with Different Chunk Sizes

1. Look at the configuration in `src/chatbot_core.py`
2. Modify `chunk_size` and `chunk_overlap` values
3. Run `python main.py --demo-docs` to see the effects
4. Understand how different settings affect chunking

### Add Your Own Documents

1. Copy PDF, TXT, or DOCX files to `sample_documents/`
2. Run `python main.py --demo-docs`
3. Observe how different document types are processed
4. Note the chunk counts and character distributions

**Ready for Stage 3?** The next stage will add semantic understanding to these processed text chunks using embeddings!

---

*This is part of the "Building an Offline LLM Chatbot" educational series. Stage 2 builds directly on Stage 1's foundation, demonstrating how to grow complex systems incrementally.* 

# Stage 3: Embeddings

## Purpose
This stage introduces embeddings, a core component of Retrieval-Augmented Generation (RAG) systems. Embeddings convert text chunks into numerical vectors, enabling efficient similarity search and retrieval.

## Why Embeddings?
Embeddings allow the chatbot to "understand" and compare the meaning of different text chunks, making it possible to retrieve relevant information for user queries.

## Model Choice
- **Model:** `all-MiniLM-L6-v2` (via HuggingFace)
- **Library:** `sentence-transformers`
- **Backend:** `torch`

### Why this model?
- Lightweight and fast
- Good balance of performance and resource usage
- Widely used in educational and production RAG systems

## New Dependencies
- `sentence-transformers`: For easy access to state-of-the-art embedding models.
- `torch`: Backend for running the model.

## How This Builds on Stage 2
- Uses the in-memory chunks from Stage 2 as input.
- Prepares for vector storage and retrieval in future stages.

---

## Changelog / What's New in Stage 3
- Introduced embedding model and vectorization logic.
- Added new dependencies.
- Updated documentation.

---

## Next Steps
- Implement embedding code.
- Add CLI/testing features for embedding generation. 