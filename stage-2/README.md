# Stage 1: Project Setup and Environment

**Building an Offline LLM Chatbot - Educational Series**

Welcome to Stage 1! This is where we build the foundation for our offline LLM chatbot. While this stage might seem simple, it establishes the architectural patterns and development practices we'll use throughout the entire series.

## 🎯 Learning Objectives

By completing Stage 1, you will:

- ✅ Set up a professional Python development environment
- ✅ Understand how to structure extensible Python projects
- ✅ Learn the importance of incremental development
- ✅ Create a foundation that will grow throughout the series
- ✅ Establish testing and configuration patterns
- ✅ Use modern Python tools like Rich for beautiful console output

## 🏗️ What We're Building

In Stage 1, we create:

1. **Project Structure** - Professional layout that scales
2. **ChatbotCore Class** - Foundation that will grow with each stage
3. **Configuration System** - Flexible settings management
4. **Testing Framework** - Verify everything works correctly
5. **Beautiful Console Output** - Using Rich for professional UX

## 📋 Prerequisites

- Python 3.11 or higher
- Basic Python knowledge (functions, classes, imports)
- Command line familiarity
- Text editor or IDE

## 🚀 Quick Start

### 1. Set Up Your Environment

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -e .
```

### 2. Run the Demo

```bash
# Basic demonstration
python main.py

# Run system tests
python main.py --test

# Show system status
python main.py --status

# Show configuration
python main.py --config
```

### 3. Expected Output

When you run `python main.py`, you should see:

```
🚀 Starting Stage 1 Demo...

🤖 Offline LLM Chatbot - Educational Series
┌─────────────────────────────────────────────────────────────────┐
│ Welcome to Stage 1: Project Setup & Environment!               │
│                                                                 │
│ 🎯 What we're building in this stage:                          │
│    • Project foundation and structure                          │
│    • Configuration management system                           │
│    • Basic logging and debugging tools                         │
│    • Environment verification                                  │
│                                                                 │
│ 🚀 What's coming in future stages:                             │
│    • Stage 2: Document processing (PDF, TXT, Markdown)         │
│    • Stage 3: Embedding and semantic similarity                │
│    • Stage 4: Vector database with ChromaDB                    │
│    • Stage 5: Local LLM integration                            │
│    • Stage 6: Complete RAG pipeline                            │
│    • Stage 7: Web interface with Streamlit                     │
│    • And more!                                                 │
│                                                                 │
│ 💡 Key Learning: We're building incrementally - each stage     │
│    adds new capabilities while maintaining what we've built    │
│    before.                                                     │
└─────────────────────────────────────────────────────────────────┘

Initializing Chatbot System...
   📋 Python version: 3.11
   ✅ rich: Available
   ✅ colorama: Available
✅ Initialization complete!

# ... plus more beautiful output showing system status
```

## 📁 Project Structure

```
stage-1/
├── src/
│   ├── __init__.py          # Package initialization
│   └── chatbot_core.py      # Main ChatbotCore class
├── main.py                  # Demo and testing script
├── pyproject.toml          # Dependencies and project config
└── README.md               # This file
```

## 🔍 Key Components Explained

### ChatbotCore Class (`src/chatbot_core.py`)

This is the heart of our system. It starts simple but is designed to grow:

```python
# Stage 1: Basic structure
chatbot = ChatbotCore()
chatbot.initialize()
print(chatbot.get_capabilities())
# Output: ['basic_setup', 'configuration', 'logging']

# Future stages will add capabilities like:
# ['document_processing', 'embeddings', 'vector_storage', 'llm_interface', 'rag_pipeline']
```

**Key Design Decisions:**
- **Extensible**: Easy to add new features in future stages
- **Testable**: Built-in testing methods
- **Configurable**: Settings that can grow with complexity
- **User-Friendly**: Rich console output for great UX

### Configuration System

Starts simple but designed to scale:

```python
# Stage 1 config
{
    "stage": 1,
    "name": "Offline LLM Chatbot",
    "version": "0.1.0",
    "debug": True
}

# Future stages will add:
# "models": {...},           # LLM model settings
# "vector_db": {...},        # ChromaDB configuration
# "documents": {...},        # Processing settings
# "embeddings": {...},       # Embedding model config
```

## 🧪 Testing

We've built comprehensive testing from the start:

```bash
# Run all tests
python main.py --test

# Tests include:
# ✅ Python version verification
# ✅ Dependency availability
# ✅ Configuration validation
# ✅ Console output system
# ✅ Capabilities reporting
```

## 💡 Key Learning Points

### 1. Incremental Development
We're not building everything at once. Each stage adds ONE major concept while building on previous work.

### 2. Architectural Thinking
Even simple code benefits from good structure. Our `ChatbotCore` class is designed to grow gracefully.

### 3. User Experience Matters
Using Rich for console output makes our tool more professional and easier to use.

### 4. Testing Early and Often
We establish testing patterns now, before complexity grows.

### 5. Documentation as You Go
Clear documentation helps others understand and contribute to your project.

## 🔮 What's Next: Stage 2 Preview

In Stage 2, we'll add document processing capabilities:

- Extract text from PDF, TXT, and Markdown files
- Learn about text chunking strategies
- Handle file metadata and processing pipelines
- Build the foundation for our knowledge base

The `ChatbotCore` class will gain new capabilities:
```python
# Stage 2 additions
chatbot.add_document("company_policy.pdf")
chunks = chatbot.get_document_chunks("company_policy.pdf")
```

## 🛠️ Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'rich'"**
```bash
# Make sure you've installed dependencies
pip install -e .
```

**"Python 3.11+ required"**
```bash
# Check your Python version
python --version

# Install Python 3.11+ if needed
# Visit: https://www.python.org/downloads/
```

**Rich output not colorful**
```bash
# Your terminal might not support colors
# Try running with --quiet flag
python main.py --quiet
```

## 🎓 Educational Notes

### For Blog Post Writers
This stage demonstrates:
- How to start a complex project simply
- The importance of good project structure
- Incremental development principles
- Testing and documentation practices

### For Learners
Focus on understanding:
- How the `ChatbotCore` class is designed to grow
- Why we're using Rich for output
- How configuration and testing work together
- The architectural decisions we're making

## 📚 Additional Resources

- [Rich Documentation](https://rich.readthedocs.io/) - Learn more about beautiful console output
- [Python Project Structure](https://docs.python-guide.org/writing/structure/) - Best practices
- [Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - Python documentation

## ✅ Stage 1 Checklist

Before moving to Stage 2, make sure:

- [ ] Python 3.11+ is installed
- [ ] Virtual environment is activated
- [ ] All dependencies install without errors
- [ ] `python main.py` runs successfully
- [ ] `python main.py --test` passes all tests
- [ ] You understand the ChatbotCore class structure
- [ ] You can see the Rich-formatted output

**Ready for Stage 2?** The next stage builds directly on this foundation by adding document processing capabilities!

---

*This is part of the "Building an Offline LLM Chatbot" educational series. Each stage builds incrementally on the previous one, teaching both AI concepts and software engineering best practices.* 