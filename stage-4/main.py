#!/usr/bin/env python3
"""
Stage 4 Demo: Vector Database Integration
Building an Offline LLM Chatbot - Educational Series

This script demonstrates Stage 4 capabilities:
- All Stage 3 functionality (maintained)
- Vector database integration (ChromaDB)
- Storing and searching embeddings
- Enhanced status reporting

NEW in Stage 4:
- Vector store demo
- Similarity search for user queries
- Enhanced architecture display

Run this script to verify your Stage 4 setup is working correctly!

Usage:
    python main.py                    # Run the basic demo
    python main.py --test             # Run system tests
    python main.py --status           # Show system status
    python main.py --config           # Show configuration
    python main.py --demo-vector      # NEW: Demo vector store and search
    python main.py --create-samples   # Create sample documents
"""

import sys
import argparse
from pathlib import Path
from typing import Dict, Any

# Add src directory to Python path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent / "src"))

from chatbot_core import ChatbotCore
from vector_store import VectorStore
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Import EmbeddingModel from stage-3
sys.path.insert(0, str(Path(__file__).parent.parent / "stage-3" / "src"))
from embedding_model import EmbeddingModel

def main():
    """Main demonstration function for Stage 4."""
    parser = argparse.ArgumentParser(
        description="Stage 4: Vector Database Integration Demo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Basic demo
  python main.py --test             # Run tests  
  python main.py --status           # Show status
  python main.py --config           # Show configuration
  python main.py --demo-vector      # Demo vector store and search
  python main.py --create-samples   # Create sample documents
        """
    )
    parser.add_argument("--test", action="store_true", help="Run system tests to verify everything is working")
    parser.add_argument("--status", action="store_true", help="Display current system status and capabilities")
    parser.add_argument("--config", action="store_true", help="Display current configuration")
    parser.add_argument("--demo-vector", action="store_true", help="NEW: Demonstrate vector store and similarity search")
    parser.add_argument("--create-samples", action="store_true", help="Create sample documents for testing")
    parser.add_argument("--quiet", action="store_true", help="Minimize output (useful for testing or many chunks)")
    args = parser.parse_args()
    console = Console()
    if not args.quiet:
        console.print("\n🚀 [bold blue]Starting Stage 4 Demo...[/bold blue]\n")
    try:
        chatbot = ChatbotCore()
        if chatbot.initialize():
            if args.test:
                run_tests(chatbot)
            elif args.status:
                show_status(chatbot)
            elif args.config:
                show_configuration(chatbot)
            elif args.demo_vector:
                demo_vector_store(chatbot)
            elif args.create_samples:
                create_sample_documents()
            else:
                run_basic_demo(chatbot)
        else:
            console.print("❌ [red]Failed to initialize chatbot system[/red]")
            sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n👋 [yellow]Demo interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n❌ [red]Error: {e}[/red]")
        sys.exit(1)

def run_basic_demo(chatbot: ChatbotCore):
    console = Console()
    demo_panel = Panel.fit(
        """
[bold green]🎉 Congratulations! Your Stage 4 setup is working perfectly![/bold green]

[bold]What we've built in Stage 4:[/bold]
✅ All Stage 3 functionality maintained
✅ Vector database integration (ChromaDB)
✅ Storing and searching embeddings
✅ Enhanced configuration system
✅ Expanded testing framework

[bold yellow]💡 Key Learning Points:[/bold yellow]
• Building incrementally: Stage 4 adds vector storage to Stage 3 foundation
• Real vector search: Retrieve relevant chunks for user queries
• Extensible design: Architecture ready for LLM integration (Stage 5)

[bold blue]🔮 Coming in Stage 5:[/bold blue]
• Local LLM integration
• Full RAG pipeline
• End-to-end retrieval and generation

[bold cyan]🧪 Try the new features:[/bold cyan]
• python main.py --demo-vector      # Vector store and search demo
• python main.py --create-samples   # Create test files
• python main.py --status           # See enhanced status

[italic]Ready for Stage 5? We'll add local LLM inference![/italic]
        """,
        title="🤖 Stage 4 Complete: Vector Database Integration!",
        border_style="green"
    )
    console.print(demo_panel)
    console.print("\n[bold]Current System Capabilities:[/bold]")
    capabilities = chatbot.get_capabilities()
    for i, capability in enumerate(capabilities, 1):
        if capability in ["vector_store", "similarity_search"]:
            console.print(f"  {i}. {capability} [green]← NEW in Stage 4![/green]")
        else:
            console.print(f"  {i}. {capability}")
    show_enhanced_architecture(console)

def demo_vector_store(chatbot: ChatbotCore):
    console = Console()
    console.print("\n[bold blue]🔎 Vector Store & Similarity Search Demo[/bold blue]\n")
    # For demo, use a few sample chunks (could be from document processing)
    chunks = [
        "The quick brown fox jumps over the lazy dog.",
        "A chatbot can use embeddings to find relevant information.",
        "Embeddings are numerical representations of text.",
        "Install the software by running the setup script.",
        "For help, consult the user manual or support page."
    ]
    model = EmbeddingModel()
    embeddings = model.embed_chunks(chunks)
    store = VectorStore()
    store.add_embeddings(chunks, embeddings)
    query = "How do I install the software?"
    results = store.query(query, model, top_k=2)
    console.print(f"\n[bold]Query:[/bold] {query}")
    console.print(f"[bold]Top results:[/bold] {results}")

def show_enhanced_architecture(console: Console):
    panel = Panel.fit(
        """
[bold]Stage 4 Architecture:[/bold]
• Document processing and chunking (Stage 2)
• Embedding generation (Stage 3)
• Vector storage and similarity search (Stage 4)
• Ready for LLM integration (Stage 5)
        """,
        title="System Architecture",
        border_style="cyan"
    )
    console.print(panel)

def create_sample_documents():
    # Reuse Stage 3's logic or provide a placeholder
    from chatbot_core import ChatbotCore
    chatbot = ChatbotCore()
    chatbot.create_sample_documents()
    print("Sample documents created.")

def run_tests(chatbot: ChatbotCore):
    print("Running system tests (placeholder for Stage 4)...")
    # You can expand this to include vector store tests
    # For now, just run the basic tests from previous stages
    chatbot.test_system()

def show_status(chatbot: ChatbotCore):
    print("System status:")
    print(chatbot.get_status())

def show_configuration(chatbot: ChatbotCore):
    print("Current configuration:")
    print(chatbot.config)

if __name__ == "__main__":
    main() 