#!/usr/bin/env python3
"""
Stage 2 Demo: Document Processing
Building an Offline LLM Chatbot - Educational Series

This script demonstrates Stage 2 capabilities:
- All Stage 1 functionality (maintained)
- Document processing (PDF, TXT, Markdown, DOCX)
- Text chunking with overlap
- File processing pipeline
- Enhanced status reporting

NEW in Stage 2:
- Document processing demo
- Sample document creation
- Document summary reporting
- Enhanced architecture display

Run this script to verify your Stage 2 setup is working correctly!

Usage:
    python main.py                    # Run the basic demo
    python main.py --test             # Run system tests
    python main.py --status           # Show system status
    python main.py --config           # Show configuration
    python main.py --demo-docs        # NEW: Demo document processing
    python main.py --create-samples   # NEW: Create sample documents
"""

import sys
import argparse
from pathlib import Path
from typing import Dict, Any

# Add src directory to Python path so we can import our modules
# Prioritize local src directory over any other paths
sys.path.insert(0, str(Path(__file__).parent / "src"))

from chatbot_core import ChatbotCore, DocumentChunk
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


def main():
    """Main demonstration function for Stage 2."""
    
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description="Stage 2: Document Processing Demo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Basic demo
  python main.py --test             # Run tests  
  python main.py --status           # Show status
  python main.py --config           # Show configuration
  python main.py --demo-docs        # Demo document processing
  python main.py --create-samples   # Create sample documents
        """
    )
    
    parser.add_argument(
        "--test", 
        action="store_true",
        help="Run system tests to verify everything is working"
    )
    
    parser.add_argument(
        "--status",
        action="store_true", 
        help="Display current system status and capabilities"
    )
    
    parser.add_argument(
        "--config",
        action="store_true",
        help="Display current configuration"
    )
    
    parser.add_argument(
        "--demo-docs",
        action="store_true",
        help="NEW: Demonstrate document processing capabilities"
    )
    
    parser.add_argument(
        "--create-samples",
        action="store_true", 
        help="NEW: Create sample documents for testing"
    )
    
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Minimize output (useful for testing or many chunks)"
    )
    
    args = parser.parse_args()
    
    # Initialize our console for rich output
    console = Console()
    
    if not args.quiet:
        console.print("\n🚀 [bold blue]Starting Stage 2 Demo...[/bold blue]\n")
    
    try:
        # Initialize the chatbot core
        # Note: In Stage 2, this now includes document processing initialization
        chatbot = ChatbotCore()
        
        # Initialize the system
        if chatbot.initialize():
            
            # Handle different command line options
            if args.test:
                run_tests(chatbot)
            elif args.status:
                show_status(chatbot)
            elif args.config:
                show_configuration(chatbot)
            elif args.demo_docs:
                demo_document_processing(chatbot)
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
    """
    Run the basic Stage 2 demonstration.
    
    Enhanced from Stage 1: Now includes document processing preview.
    """
    console = Console()
    
    # Show what we've accomplished in Stage 2
    demo_panel = Panel.fit(
        """
[bold green]🎉 Congratulations! Your Stage 2 setup is working perfectly![/bold green]

[bold]What we've built in Stage 2:[/bold]
✅ All Stage 1 functionality maintained
✅ Document processing (PDF, TXT, Markdown, DOCX)
✅ Smart text chunking with overlap
✅ File processing pipeline
✅ Enhanced configuration system
✅ Expanded testing framework

[bold yellow]💡 Key Learning Points:[/bold yellow]
• Building incrementally: Stage 2 adds document processing to Stage 1 foundation
• Real file processing: Extract text from multiple document formats
• Smart chunking: Prepare text for future AI processing
• Extensible design: Architecture ready for embeddings (Stage 3)

[bold blue]🔮 Coming in Stage 3:[/bold blue]
• Semantic embeddings with sentence-transformers
• Text similarity search
• Foundation for vector databases
• Preparing for RAG pipeline

[bold cyan]🧪 Try the new features:[/bold cyan]
• python main.py --demo-docs        # Process sample documents
• python main.py --create-samples   # Create test files
• python main.py --status           # See enhanced status

[italic]Ready for Stage 3? We'll add semantic search to these documents![/italic]
        """,
        title="🤖 Stage 2 Complete: Document Processing!",
        border_style="green"
    )
    
    console.print(demo_panel)
    
    # Show current capabilities (enhanced from Stage 1)
    console.print("\n[bold]Current System Capabilities:[/bold]")
    capabilities = chatbot.get_capabilities()
    for i, capability in enumerate(capabilities, 1):
        if capability in ["document_processing", "text_chunking"]:
            console.print(f"  {i}. {capability} [green]← NEW in Stage 2![/green]")
        else:
            console.print(f"  {i}. {capability}")
    
    # Enhanced architecture preview
    show_enhanced_architecture(console)
    
    # Show document processing preview
    show_document_processing_preview(console)


def show_enhanced_architecture(console: Console):
    """Show the enhanced system architecture for Stage 2."""
    console.print("\n[bold]Enhanced System Architecture:[/bold]")
    architecture_table = Table(show_header=True, header_style="bold magenta")
    architecture_table.add_column("Component", style="cyan")
    architecture_table.add_column("Stage 2 Status", style="green")
    architecture_table.add_column("Future Enhancements", style="yellow")
    
    architecture_table.add_row(
        "ChatbotCore", 
        "✅ Enhanced with document processing", 
        "Will add embeddings, LLM, RAG"
    )
    architecture_table.add_row(
        "Configuration", 
        "✅ Document processing settings", 
        "Model configs, DB settings, etc."
    )
    architecture_table.add_row(
        "Document Processing", 
        "✅ PDF, TXT, Markdown, DOCX", 
        "Enhanced extraction, preprocessing"
    )
    architecture_table.add_row(
        "Text Chunking", 
        "✅ Smart overlap strategy", 
        "Semantic chunking, optimization"
    )
    architecture_table.add_row(
        "Testing", 
        "✅ Document processing tests", 
        "Integration tests, edge cases"
    )
    architecture_table.add_row(
        "Embeddings", 
        "🔮 Coming in Stage 3", 
        "Sentence transformers, similarity"
    )
    architecture_table.add_row(
        "Vector Database", 
        "🔮 Coming in Stage 4", 
        "ChromaDB integration"
    )
    architecture_table.add_row(
        "Local LLM", 
        "🔮 Coming in Stage 5", 
        "GGUF model support"
    )
    
    console.print(architecture_table)


def show_document_processing_preview(console: Console):
    """Show a preview of document processing capabilities."""
    console.print("\n[bold]Document Processing Capabilities:[/bold]")
    
    formats_table = Table(show_header=True, header_style="bold blue")
    formats_table.add_column("File Format", style="cyan")
    formats_table.add_column("Extension", style="yellow")
    formats_table.add_column("Processing Method", style="green")
    
    formats_table.add_row("PDF Documents", ".pdf", "pypdf extraction")
    formats_table.add_row("Text Files", ".txt", "Direct reading")
    formats_table.add_row("Markdown", ".md, .markdown", "Markdown processing")
    formats_table.add_row("Word Documents", ".docx", "python-docx extraction")
    
    console.print(formats_table)
    
    console.print("\n[italic yellow]💡 Tip: Try 'python main.py --create-samples' to create test documents![/italic yellow]")


def demo_document_processing(chatbot: ChatbotCore):
    """NEW in Stage 2: Demonstrate document processing capabilities."""
    console = Console()
    
    console.print("\n[bold blue]🔧 Document Processing Demo[/bold blue]\n")
    
    # Check if sample documents exist
    sample_dir = Path("sample_documents")
    if not sample_dir.exists():
        console.print("[yellow]📝 No sample documents found. Creating samples...[/yellow]")
        create_sample_documents()
    
    # Process sample documents with simple, fast output
    processed_count = 0
    total_chunks = 0
    
    console.print("[yellow]Processing documents...[/yellow]")
    
    for file_path in sample_dir.glob("*"):
        if file_path.suffix.lower() in chatbot.supported_formats:
            try:
                # Process document quietly (without verbose console output)
                chunks = process_document_quietly(chatbot, str(file_path))
                processed_count += 1
                total_chunks += len(chunks)
                
                # Show concise progress immediately
                console.print(f"✅ [cyan]{file_path.name}[/cyan]: {len(chunks)} chunks, {sum(len(c.text) for c in chunks):,} chars")
                
                # Show preview only for first document or if very few chunks
                if processed_count == 1 or len(chunks) <= 3:
                    if chunks:
                        first_chunk = chunks[0]
                        preview = first_chunk.text[:100] + "..." if len(first_chunk.text) > 100 else first_chunk.text
                        console.print(f"   📝 Preview: [italic dim]{preview}[/italic dim]")
                
            except Exception as e:
                console.print(f"❌ [red]Error processing {file_path.name}: {e}[/red]")
    
    if processed_count > 0:
        # Show efficient summary
        console.print(f"\n[bold green]📊 Processing Complete![/bold green]")
        summary = chatbot.get_document_summary()
        
        # Compact summary table
        summary_table = Table(show_header=True, header_style="bold magenta", show_lines=True)
        summary_table.add_column("Metric", style="cyan", width=18)
        summary_table.add_column("Value", style="green", justify="right", width=12)
        
        summary_table.add_row("Documents", str(summary["total_documents"]))
        summary_table.add_row("Total Chunks", str(summary["total_chunks"]))
        summary_table.add_row("Total Characters", f"{summary['total_characters']:,}")
        
        # Calculate average chunk size
        avg_chunk_size = summary['total_characters'] // summary['total_chunks'] if summary['total_chunks'] > 0 else 0
        summary_table.add_row("Avg Chunk Size", f"{avg_chunk_size:,} chars")
        
        console.print(summary_table)
        
        # Show per-document details in a more compact format
        if summary["documents"]:
            console.print("\n[bold]Document Breakdown:[/bold]")
            doc_table = Table(show_header=True, header_style="bold blue", show_lines=False)
            doc_table.add_column("Document", style="cyan", width=20)
            doc_table.add_column("Chunks", style="yellow", justify="right", width=8)
            doc_table.add_column("Characters", style="green", justify="right", width=12)
            doc_table.add_column("Avg Size", style="dim", justify="right", width=10)
            
            for doc_name, details in summary["documents"].items():
                avg_size = details['characters'] // details['chunks'] if details['chunks'] > 0 else 0
                doc_table.add_row(
                    doc_name,
                    str(details["chunks"]),
                    f"{details['characters']:,}",
                    f"{avg_size:,}"
                )
            
            console.print(doc_table)
            
        # Show tip for larger files
        if total_chunks > 10:
            console.print(f"\n[dim]💡 Tip: With {total_chunks} chunks total, this demonstrates how the system handles larger documents efficiently![/dim]")
    else:
        console.print("[yellow]⚠️ No documents were processed. Try creating samples first.[/yellow]")


def process_document_quietly(chatbot: ChatbotCore, file_path: str):
    """Process a document without verbose console output - fast and simple."""
    file_path = Path(file_path)
    
    # Quick validation
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if file_path.suffix.lower() not in chatbot.supported_formats:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")
    
    # Extract text based on file type (simplified, no console output)
    try:
        if file_path.suffix.lower() == '.pdf':
            text = chatbot._extract_pdf_text(file_path)
        elif file_path.suffix.lower() == '.docx':
            text = chatbot._extract_docx_text(file_path)
        elif file_path.suffix.lower() in ['.md', '.markdown']:
            text = chatbot._extract_markdown_text(file_path)
        elif file_path.suffix.lower() == '.txt':
            text = chatbot._extract_txt_text(file_path)
        else:
            raise ValueError(f"Unsupported format: {file_path.suffix}")
        
        # Create chunks from extracted text (this should be fast)
        chunks = chatbot._create_text_chunks(text, str(file_path))
        
        # Store processed document
        chatbot.processed_documents[file_path.name] = chunks
        
        return chunks
        
    except Exception as e:
        # Don't let any single document crash the whole process
        raise RuntimeError(f"Failed to process {file_path.name}: {e}")


def create_sample_documents():
    """NEW in Stage 2: Create sample documents for testing."""
    console = Console()
    
    console.print("\n[bold blue]📝 Creating Sample Documents[/bold blue]\n")
    
    sample_dir = Path("sample_documents")
    sample_dir.mkdir(exist_ok=True)
    
    # Sample documents content
    samples = {
        "company_policy.txt": """
Company Employee Handbook

Welcome to our company! This handbook contains important policies and procedures.

VACATION POLICY:
All employees are entitled to 15 days of paid vacation per year. Vacation requests must be submitted at least 2 weeks in advance. Vacation time cannot be carried over to the next year.

REMOTE WORK POLICY:
Employees may work remotely up to 2 days per week with manager approval. Remote work must be arranged in advance and productivity standards must be maintained.

IT SECURITY:
All employees must use strong passwords and enable two-factor authentication. Company devices should not be used for personal activities. Report any security incidents immediately.

BENEFITS:
The company provides health insurance, dental coverage, and a 401k plan with company matching up to 4% of salary.
        """,
        
        "technical_guide.md": """
# Technical Setup Guide

## Overview
This guide will help you set up your development environment.

## Prerequisites
- Python 3.11 or higher
- Git installed
- Code editor (VS Code recommended)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/company/project.git
cd project
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
Edit the `config.yaml` file with your settings:
- Database URL
- API keys
- Environment variables

## Testing
Run the test suite:
```bash
pytest tests/
```

## Troubleshooting
Common issues and solutions:
- **Import errors**: Check your Python path
- **Permission denied**: Ensure proper file permissions
- **Module not found**: Verify virtual environment is activated
        """,
        
        "meeting_notes.txt": """
Team Meeting Notes - January 15, 2024

Attendees: Alice, Bob, Carol, Dave

AGENDA:
1. Project status update
2. Q1 planning
3. Technical debt review
4. Action items

PROJECT STATUS:
- Phase 1 completed on time
- Phase 2 is 80% complete, expected completion next week
- No major blockers identified

Q1 PLANNING:
- Focus on user experience improvements
- Plan for mobile app development
- Increase test coverage to 90%

TECHNICAL DEBT:
- Refactor authentication system (Priority: High)
- Update dependencies (Priority: Medium)
- Improve error handling (Priority: Medium)

ACTION ITEMS:
1. Alice: Complete Phase 2 by Friday
2. Bob: Begin mobile app wireframes
3. Carol: Audit current test coverage
4. Dave: Research authentication frameworks

NEXT MEETING: January 22, 2024
        """
    }
    
    # Create sample files
    for filename, content in samples.items():
        file_path = sample_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        console.print(f"✅ Created: {filename}")
    
    console.print(f"\n[green]📁 Sample documents created in: {sample_dir.absolute()}[/green]")
    console.print("[italic yellow]💡 Try: python main.py --demo-docs[/italic yellow]")


def run_tests(chatbot: ChatbotCore):
    """Run comprehensive system tests (enhanced from Stage 1)."""
    console = Console()
    
    console.print("\n🧪 [bold]Running Comprehensive Stage 2 Tests...[/bold]\n")
    
    # Run the chatbot's built-in tests
    tests_passed = chatbot.test_system()
    
    # Additional Stage 2 specific tests
    console.print("[yellow]Running additional Stage 2 tests...[/yellow]")
    
    try:
        # Test document processing dependencies
        import pypdf
        import docx
        import markdown
        console.print("   ✅ All document processing dependencies available")
        
        # Test document configuration
        config = chatbot.config
        assert config["stage"] == 2
        assert "documents" in config
        console.print("   ✅ Stage 2 configuration valid")
        
        # Test new capabilities
        capabilities = chatbot.get_capabilities()
        assert "document_processing" in capabilities
        assert "text_chunking" in capabilities
        console.print("   ✅ New Stage 2 capabilities present")
        
        # Test document processing with sample text
        sample_text = "This is a test document for Stage 2. " * 50
        chunks = chatbot._create_text_chunks(sample_text, "test.txt")
        assert len(chunks) > 0
        console.print(f"   ✅ Text chunking working (created {len(chunks)} chunks)")
        
        console.print("\n✅ [bold green]All Stage 2 tests passed![/bold green]")
        
    except Exception as e:
        console.print(f"\n❌ [red]Stage 2 tests failed: {e}[/red]")
        tests_passed = False
    
    # Summary
    if tests_passed:
        console.print("\n🎉 [bold green]Your Stage 2 setup is perfect! Ready for Stage 3.[/bold green]")
    else:
        console.print("\n⚠️ [bold yellow]Some tests failed. Check your setup.[/bold yellow]")


def show_status(chatbot: ChatbotCore):
    """Display detailed system status (enhanced from Stage 1)."""
    console = Console()
    
    status = chatbot.get_status()
    
    # Basic status information
    basic_info = f"""
[bold]System Status Report[/bold]

[bold blue]Basic Information:[/bold blue]
  • Stage: {status['stage']} (Document Processing)
  • Initialized: {'✅ Yes' if status['initialized'] else '❌ No'}
  • Name: {status['config']['name']}
  • Version: {status['config']['version']}

[bold blue]Current Capabilities:[/bold blue]
{chr(10).join(f'  • {cap}' for cap in status['capabilities'])}

[bold blue]Configuration Keys:[/bold blue]
{chr(10).join(f'  • {key}' for key in status['config'].keys())}
    """
    
    # Add document processing status if available
    if 'documents' in status:
        doc_info = status['documents']
        basic_info += f"""

[bold blue]Document Processing Status:[/bold blue]
  • Documents Processed: {doc_info['total_documents']}
  • Total Chunks: {doc_info['total_chunks']}
  • Total Characters: {doc_info['total_characters']:,}
"""
    
    basic_info += """

[bold yellow]Next Steps:[/bold yellow]
  Ready to move to Stage 3: Embeddings and Semantic Similarity!
    """
    
    status_panel = Panel.fit(
        basic_info,
        title="🔍 Enhanced System Status",
        border_style="blue"
    )
    
    console.print(status_panel)


def show_configuration(chatbot: ChatbotCore):
    """Display current configuration in detail (enhanced from Stage 1)."""
    console = Console()
    
    # Basic configuration table
    config_table = Table(show_header=True, header_style="bold magenta")
    config_table.add_column("Setting", style="cyan")
    config_table.add_column("Value", style="green")
    config_table.add_column("Description", style="yellow")
    
    config = chatbot.config
    
    config_table.add_row("stage", str(config["stage"]), "Current stage number")
    config_table.add_row("name", config["name"], "Project name")
    config_table.add_row("version", config["version"], "Current version")
    config_table.add_row("debug", str(config["debug"]), "Debug mode enabled")
    
    console.print("\n[bold]Basic Configuration:[/bold]")
    console.print(config_table)
    
    # Stage 2 NEW: Document processing configuration
    if "documents" in config:
        doc_config = config["documents"]
        
        doc_table = Table(show_header=True, header_style="bold blue")
        doc_table.add_column("Document Setting", style="cyan")
        doc_table.add_column("Value", style="green")
        doc_table.add_column("Description", style="yellow")
        
        doc_table.add_row("chunk_size", str(doc_config["chunk_size"]), "Characters per chunk")
        doc_table.add_row("chunk_overlap", str(doc_config["chunk_overlap"]), "Character overlap between chunks")
        doc_table.add_row("min_chunk_size", str(doc_config["min_chunk_size"]), "Minimum chunk size")
        
        console.print("\n[bold]Document Processing Configuration:[/bold]")
        console.print(doc_table)
        
        # Supported formats
        formats = ", ".join(doc_config["supported_formats"])
        console.print(f"\n[bold blue]Supported Formats:[/bold blue] {formats}")
    
    console.print("\n[italic yellow]Note: Configuration will continue expanding in future stages![/italic yellow]")


if __name__ == "__main__":
    main() 