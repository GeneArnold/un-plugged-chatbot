# Offline LLM Chatbot (Simple RAG Pipeline)

This project is a simple Retrieval-Augmented Generation (RAG) chatbot that can answer questions using your own documents. It supports both a local Llama model and OpenAI's GPT-3.5-turbo.

## Features
- **Document Ingestion:** Reads `.txt` and `.md` files from the `sample_docs/` directory.
- **Chunking:** Splits documents into overlapping text chunks for better retrieval.
- **Embeddings:** Uses `sentence-transformers` to embed chunks.
- **Vector Search:** Stores and retrieves chunks using ChromaDB for relevant context.
- **LLM Answering:**
  - **Local:** Uses a Llama model (via `llama-cpp-python`).
  - **Cloud:** Uses OpenAI's GPT-3.5-turbo (requires API key).
- **User Feedback:** Shows a spinner and message while the model is generating an answer, so you know the app is working.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your documents:**
   - Place `.txt` or `.md` files in the `sample_docs/` folder.

3. **Download a Llama model:**
   - Place your GGUF model file (e.g., `llama-2-7b.Q4_0.gguf`) in the `models/` directory.

4. **(Optional) Set your OpenAI API key:**
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

5. **Run the chatbot:**
   ```bash
   python main.py
   ```

6. **Ask questions:**
   - The script will show available files, chunk them, and let you ask a question.
   - Choose which model to use (local Llama or OpenAI).
   - A spinner will show while the model is thinking.

## Notes
- The code is portable and does not use hardcoded paths.
- The spinner works for all models and displays which model is running.
- To suppress Hugging Face tokenizer warnings, the script sets `TOKENIZERS_PARALLELISM=false` automatically.

## Requirements
- Python 3.11+
- See `requirements.txt` for dependencies.

---

This is a minimal, educational example. For more advanced features, see the project blog or future updates!

