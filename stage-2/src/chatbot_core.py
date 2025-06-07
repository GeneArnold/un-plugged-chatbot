"""
ChatbotCore - Foundation Class for Our Offline LLM Chatbot

This is the core class that will grow throughout our blog series.
In Stage 1: Basic structure and configuration
In Stage 2: Document processing capabilities  
In Stage 3: Embedding and similarity features
In Stage 4: Vector storage integration
In Stage 5: Local LLM integration
In Stage 6: Complete RAG pipeline
... and so on

This demonstrates how to build complex systems incrementally!
"""

from typing import Dict, Any, Optional, List
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from pathlib import Path
import os

# Stage 2 NEW: Document processing imports
import pypdf
from docx import Document as DocxDocument
import markdown


class DocumentChunk:
    """
    Represents a chunk of text from a processed document.
    
    Stage 2 NEW: This class encapsulates document chunks with metadata.
    In Stage 3, we'll add embedding capabilities to these chunks.
    In Stage 4, we'll store these in a vector database.
    """
    
    def __init__(self, text: str, source_file: str, chunk_index: int, 
                 start_char: int = 0, end_char: int = 0):
        self.text = text
        self.source_file = source_file
        self.chunk_index = chunk_index
        self.start_char = start_char
        self.end_char = end_char
        self.metadata = {
            "source": source_file,
            "chunk_index": chunk_index,
            "length": len(text),
            "start_char": start_char,
            "end_char": end_char
        }
    
    def __repr__(self) -> str:
        return f"DocumentChunk(source='{self.source_file}', index={self.chunk_index}, length={len(self.text)})"


class ChatbotCore:
    """
    The foundation class for our offline LLM chatbot.
    
    This class starts simple but will grow significantly as we add:
    - Document processing (Stage 2)
    - Embeddings (Stage 3) 
    - Vector storage (Stage 4)
    - Local LLM (Stage 5)
    - RAG pipeline (Stage 6)
    - Web interface (Stage 7)
    - And more!
    
    Design Philosophy:
    - Start simple, grow gradually
    - Each stage adds new capabilities
    - Maintain backwards compatibility
    - Clear separation of concerns
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the ChatbotCore.
        
        Args:
            config (Dict): Configuration dictionary (optional)
                          If None, will use default configuration
        """
        # Initialize the rich console for beautiful output
        self.console = Console()
        
        # Set up configuration (now includes document processing settings)
        self.config = config or self._get_default_config()
        
        # Initialize basic state
        self.is_initialized = False
        self.stage = 2  # Updated for Stage 2
        self.capabilities = [
            "basic_setup", 
            "configuration", 
            "logging",
            "document_processing",  # NEW in Stage 2
            "text_chunking"         # NEW in Stage 2
        ]
        
        # Stage 2 NEW: Document storage
        self.processed_documents = {}  # filename -> list of DocumentChunk
        self.supported_formats = ['.pdf', '.txt', '.md', '.markdown', '.docx']
        
        # Display welcome message
        self._display_welcome()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """
        Get the default configuration for Stage 2.
        
        Enhanced from Stage 1: Now includes document processing settings.
        This shows how configuration grows naturally with new features.
        
        Returns:
            Dict: Default configuration dictionary
        """
        return {
            "stage": 2,  # Updated for Stage 2
            "name": "Offline LLM Chatbot",
            "version": "0.2.0",  # Updated version
            "debug": True,
            
            # Stage 2 NEW: Document processing configuration
            "documents": {
                "chunk_size": 500,        # Characters per chunk
                "chunk_overlap": 200,      # Character overlap between chunks
                "min_chunk_size": 100,     # Minimum chunk size
                "supported_formats": ['.pdf', '.txt', '.md', '.markdown', '.docx']
            },
            
            # These will be populated in later stages:
            # "embeddings": {...},       # Stage 3: Embedding model settings
            # "vector_db": {...},        # Stage 4: ChromaDB settings  
            # "models": {...},           # Stage 5: LLM model settings
            # "web_interface": {...},    # Stage 7: Streamlit settings
        }
    
    def _display_welcome(self):
        """Display a welcome message explaining what this stage does."""
        welcome_text = f"""
[bold green]Welcome to Stage {self.stage}: Document Processing![/bold green]

🎯 [bold]What we're building in this stage:[/bold]
   • Document text extraction (PDF, TXT, Markdown, DOCX)
   • Smart text chunking with overlap
   • File processing pipeline
   • Knowledge base foundation

🔧 [bold]Enhanced from Stage 1:[/bold]
   • All Stage 1 functionality maintained
   • Extended ChatbotCore class with new methods
   • Enhanced configuration system
   • Additional testing capabilities

🚀 [bold]What's coming in future stages:[/bold]
   • Stage 3: Embedding and semantic similarity
   • Stage 4: Vector database with ChromaDB
   • Stage 5: Local LLM integration
   • Stage 6: Complete RAG pipeline
   • Stage 7: Web interface with Streamlit
   • And more!

💡 [bold]Key Learning:[/bold] We're building incrementally - Stage 2 adds 
   document processing while keeping everything from Stage 1 working.
        """
        
        panel = Panel(
            welcome_text,
            title="🤖 Offline LLM Chatbot - Educational Series",
            border_style="blue",
            padding=(1, 2)
        )
        self.console.print(panel)
    
    def initialize(self) -> bool:
        """
        Initialize the chatbot system.
        
        Enhanced from Stage 1: Now includes document processor initialization.
        This demonstrates incremental feature addition.
        
        Returns:
            bool: True if initialization successful
        """
        try:
            self.console.print("\n[yellow]Initializing Chatbot System...[/yellow]")
            
            # Stage 1: Basic environment checks
            self._check_python_version()
            self._check_dependencies()
            
            # Stage 2 NEW: Initialize document processor
            self._initialize_document_processor()  # Implemented from Stage 1 extension point!
            
            # In future stages, we'll add:
            # self._initialize_embeddings()          # Stage 3
            # self._initialize_vector_store()        # Stage 4
            # self._initialize_llm()                 # Stage 5
            # self._initialize_rag_pipeline()        # Stage 6
            
            self.is_initialized = True
            self.console.print("✅ [green]Initialization complete![/green]\n")
            return True
            
        except Exception as e:
            self.console.print(f"❌ [red]Initialization failed: {e}[/red]\n")
            return False
    
    def _check_python_version(self):
        """Verify we're running on Python 3.11+"""
        import sys
        
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.console.print(f"   📋 Python version: {python_version}")
        
        if sys.version_info < (3, 11):
            raise RuntimeError(f"Python 3.11+ required, found {python_version}")
    
    def _check_dependencies(self):
        """Check that our dependencies are available"""
        dependencies = ["rich", "colorama"]
        
        for dep in dependencies:
            try:
                __import__(dep)
                self.console.print(f"   ✅ {dep}: Available")
            except ImportError:
                raise RuntimeError(f"Required dependency '{dep}' not found")
    
    def _initialize_document_processor(self):
        """
        Stage 2 NEW: Initialize the document processing system.
        
        This was an extension point in Stage 1 - now we implement it!
        Shows how our architecture enables smooth feature addition.
        """
        self.console.print(f"   🔧 Document processor: Ready")
        self.console.print(f"   📄 Supported formats: {', '.join(self.supported_formats)}")
        
        # Validate document configuration
        doc_config = self.config.get("documents", {})
        chunk_size = doc_config.get("chunk_size", 1000)
        chunk_overlap = doc_config.get("chunk_overlap", 200)
        
        if chunk_overlap >= chunk_size:
            raise RuntimeError(f"Chunk overlap ({chunk_overlap}) must be less than chunk size ({chunk_size})")
        
        self.console.print(f"   📏 Chunk size: {chunk_size} chars, overlap: {chunk_overlap} chars")
    
    # ========== Stage 2 NEW: Document Processing Methods ==========
    
    def process_document(self, file_path: str) -> List[DocumentChunk]:
        """
        Process a document and return text chunks.
        
        This is the main document processing method that supports multiple formats.
        
        Args:
            file_path (str): Path to the document file
            
        Returns:
            List[DocumentChunk]: List of text chunks with metadata
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is not supported
        """
        if not self.is_initialized:
            raise RuntimeError("ChatbotCore must be initialized before processing documents")
        
        file_path = Path(file_path)
        
        # Validate file exists
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Check if format is supported
        if file_path.suffix.lower() not in self.supported_formats:
            raise ValueError(f"Unsupported file format: {file_path.suffix}. Supported: {self.supported_formats}")
        
        self.console.print(f"\n[cyan]Processing document: {file_path.name}[/cyan]")
        
        # Extract text based on file type
        try:
            if file_path.suffix.lower() == '.pdf':
                text = self._extract_pdf_text(file_path)
            elif file_path.suffix.lower() == '.docx':
                text = self._extract_docx_text(file_path)
            elif file_path.suffix.lower() in ['.md', '.markdown']:
                text = self._extract_markdown_text(file_path)
            elif file_path.suffix.lower() == '.txt':
                text = self._extract_txt_text(file_path)
            else:
                raise ValueError(f"Unsupported format: {file_path.suffix}")
            
            # Create chunks from extracted text
            chunks = self._create_text_chunks(text, str(file_path))
            
            # Store processed document
            self.processed_documents[file_path.name] = chunks
            
            self.console.print(f"✅ Processed {file_path.name}: {len(chunks)} chunks, {len(text)} characters")
            
            return chunks
            
        except Exception as e:
            self.console.print(f"❌ [red]Error processing {file_path.name}: {e}[/red]")
            raise
    
    def _extract_pdf_text(self, file_path: Path) -> str:
        """Extract text from PDF file using pypdf."""
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                text += page_text + "\n"
        return text.strip()
    
    def _extract_docx_text(self, file_path: Path) -> str:
        """Extract text from DOCX file using python-docx."""
        doc = DocxDocument(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    
    def _extract_markdown_text(self, file_path: Path) -> str:
        """Extract text from Markdown file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()
        
        # Convert markdown to plain text (removes formatting)
        html = markdown.markdown(md_content)
        # For now, return the raw markdown (in Stage 3, we might improve this)
        return md_content
    
    def _extract_txt_text(self, file_path: Path) -> str:
        """Extract text from plain text file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def _create_text_chunks(self, text: str, source_file: str) -> List[DocumentChunk]:
        """
        Split text into overlapping chunks.
        This implements smart chunking strategy that will be crucial for RAG in later stages.
        FIX: Prevent infinite loop by ensuring start always advances.
        """
        doc_config = self.config["documents"]
        chunk_size = doc_config["chunk_size"]
        overlap = doc_config["chunk_overlap"]
        min_size = doc_config["min_chunk_size"]
        
        if len(text) <= chunk_size:
            # Text is small enough to be one chunk
            return [DocumentChunk(text, source_file, 0, 0, len(text))]
        
        chunks = []
        start = 0
        chunk_index = 0
        
        while start < len(text):
            # Calculate end position
            end = min(start + chunk_size, len(text))
            
            # Extract chunk text
            chunk_text = text[start:end].strip()
            
            # Only create chunk if it meets minimum size
            if len(chunk_text) >= min_size:
                chunks.append(DocumentChunk(
                    text=chunk_text,
                    source_file=source_file,
                    chunk_index=chunk_index,
                    start_char=start,
                    end_char=end
                ))
                chunk_index += 1
            
            # FIX: Prevent infinite loop by ensuring we always advance
            next_start = end - overlap
            if next_start <= start:
                break
            start = next_start
        
        return chunks
    
    def get_processed_documents(self) -> Dict[str, List[DocumentChunk]]:
        """Get all processed documents and their chunks."""
        return self.processed_documents.copy()
    
    def get_document_summary(self) -> Dict[str, Any]:
        """Get summary of processed documents."""
        total_chunks = sum(len(chunks) for chunks in self.processed_documents.values())
        total_chars = sum(
            sum(len(chunk.text) for chunk in chunks) 
            for chunks in self.processed_documents.values()
        )
        
        return {
            "total_documents": len(self.processed_documents),
            "total_chunks": total_chunks,
            "total_characters": total_chars,
            "documents": {
                name: {
                    "chunks": len(chunks),
                    "characters": sum(len(chunk.text) for chunk in chunks)
                }
                for name, chunks in self.processed_documents.items()
            }
        }
    
    # ========== Enhanced Stage 1 Methods ==========
    
    def get_capabilities(self) -> list:
        """
        Get current system capabilities.
        
        Enhanced from Stage 1: Now includes document processing capabilities!
        
        Returns:
            list: Current capabilities
        """
        return self.capabilities.copy()
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current system status.
        
        Enhanced from Stage 1: Now includes document processing status.
        
        Returns:
            Dict: Status information
        """
        status = {
            "stage": self.stage,
            "initialized": self.is_initialized,
            "capabilities": self.get_capabilities(),
            "config": self.config
        }
        
        # Stage 2 NEW: Add document processing status
        if self.processed_documents:
            status["documents"] = self.get_document_summary()
        
        return status
    
    def test_system(self) -> bool:
        """
        Test that the system is working correctly.
        
        Enhanced from Stage 1: Now includes document processing tests.
        
        Returns:
            bool: True if all tests pass
        """
        self.console.print("\n[yellow]Running system tests...[/yellow]")
        
        tests = [
            ("Configuration", self._test_config),
            ("Console Output", self._test_console),
            ("Document Processing", self._test_documents),     # NEW in Stage 2
            # Future stages will add:
            # ("Embeddings", self._test_embeddings),            # Stage 3
            # ("Vector Store", self._test_vector_store),        # Stage 4
            # ("LLM Interface", self._test_llm),                # Stage 5
            # ("RAG Pipeline", self._test_rag_pipeline),        # Stage 6
        ]
        
        all_passed = True
        for test_name, test_func in tests:
            try:
                test_func()
                self.console.print(f"   ✅ {test_name}: PASSED")
            except Exception as e:
                self.console.print(f"   ❌ {test_name}: FAILED - {e}")
                all_passed = False
        
        status = "PASSED" if all_passed else "FAILED"
        color = "green" if all_passed else "red"
        self.console.print(f"\n[{color}]Overall test result: {status}[/{color}]\n")
        
        return all_passed
    
    def _test_config(self):
        """Test configuration system"""
        assert self.config is not None
        assert "stage" in self.config
        assert self.config["stage"] == 2  # Updated for Stage 2
        
        # Stage 2 NEW: Test document configuration
        assert "documents" in self.config
        assert "chunk_size" in self.config["documents"]
        assert "chunk_overlap" in self.config["documents"]
    
    def _test_console(self):
        """Test console output system"""
        # Test that we can create formatted output
        test_panel = Panel("Test output", title="Test")
        # Note: We don't actually print it during tests 
    
    def _test_documents(self):
        """
        Stage 2 NEW: Test document processing system.
        
        This test verifies that document processing capabilities work correctly.
        """
        # Test that document processor is initialized
        assert hasattr(self, 'supported_formats')
        assert len(self.supported_formats) > 0
        
        # Test configuration validation
        doc_config = self.config.get("documents", {})
        assert "chunk_size" in doc_config
        assert "chunk_overlap" in doc_config
        assert doc_config["chunk_overlap"] < doc_config["chunk_size"]
        
        # Test text chunking with sample text
        sample_text = "This is a test document. " * 100  # Repeating text
        chunks = self._create_text_chunks(sample_text, "test.txt")
        assert len(chunks) > 0
        assert all(isinstance(chunk, DocumentChunk) for chunk in chunks)
        
        # Test chunk metadata
        first_chunk = chunks[0]
        assert first_chunk.source_file == "test.txt"
        assert first_chunk.chunk_index == 0
        assert len(first_chunk.text) > 0 