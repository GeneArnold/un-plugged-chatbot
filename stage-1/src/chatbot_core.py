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

from typing import Dict, Any, Optional
from rich.console import Console
from rich.panel import Panel
import os


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
        
        # Set up basic configuration
        # In later stages, this will include model paths, database settings, etc.
        self.config = config or self._get_default_config()
        
        # Initialize basic state
        self.is_initialized = False
        self.stage = 1
        self.capabilities = ["basic_setup", "configuration", "logging"]
        
        # Display welcome message
        self._display_welcome()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """
        Get the default configuration for Stage 1.
        
        In later stages, this will include:
        - Model download URLs and paths
        - Vector database settings  
        - Chunk sizes and overlap settings
        - LLM generation parameters
        - Web interface settings
        
        Returns:
            Dict: Default configuration dictionary
        """
        return {
            "stage": 1,
            "name": "Offline LLM Chatbot",
            "version": "0.1.0",
            "debug": True,
            
            # These will be populated in later stages:
            # "models": {...},           # Stage 5: LLM model settings
            # "vector_db": {...},        # Stage 4: ChromaDB settings  
            # "documents": {...},        # Stage 2: Document processing
            # "embeddings": {...},       # Stage 3: Embedding model settings
            # "web_interface": {...},    # Stage 7: Streamlit settings
        }
    
    def _display_welcome(self):
        """Display a welcome message explaining what this stage does."""
        welcome_text = f"""
[bold green]Welcome to Stage {self.stage}: Project Setup & Environment![/bold green]

🎯 [bold]What we're building in this stage:[/bold]
   • Project foundation and structure
   • Configuration management system
   • Basic logging and debugging tools
   • Environment verification

🚀 [bold]What's coming in future stages:[/bold]
   • Stage 2: Document processing (PDF, TXT, Markdown)
   • Stage 3: Embedding and semantic similarity
   • Stage 4: Vector database with ChromaDB
   • Stage 5: Local LLM integration
   • Stage 6: Complete RAG pipeline
   • Stage 7: Web interface with Streamlit
   • And more!

💡 [bold]Key Learning:[/bold] We're building incrementally - each stage
   adds new capabilities while maintaining what we've built before.
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
        
        In Stage 1: Just basic checks
        In later stages: Initialize models, databases, etc.
        
        Returns:
            bool: True if initialization successful
        """
        try:
            self.console.print("\n[yellow]Initializing Chatbot System...[/yellow]")
            
            # Stage 1: Basic environment checks
            self._check_python_version()
            self._check_dependencies()
            
            # In future stages, we'll add:
            # self._initialize_document_processor()  # Stage 2
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
    
    def get_capabilities(self) -> list:
        """
        Get current system capabilities.
        
        This list will grow significantly in later stages!
        
        Returns:
            list: Current capabilities
        """
        return self.capabilities.copy()
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current system status.
        
        Returns:
            Dict: Status information
        """
        return {
            "stage": self.stage,
            "initialized": self.is_initialized,
            "capabilities": self.get_capabilities(),
            "config": self.config
        }
    
    def test_system(self) -> bool:
        """
        Test that the system is working correctly.
        
        In Stage 1: Basic functionality tests
        In later stages: Test all components
        
        Returns:
            bool: True if all tests pass
        """
        self.console.print("\n[yellow]Running system tests...[/yellow]")
        
        tests = [
            ("Configuration", self._test_config),
            ("Console Output", self._test_console),
            # Future stages will add:
            # ("Document Processing", self._test_documents),     # Stage 2
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
        assert self.config["stage"] == 1
    
    def _test_console(self):
        """Test console output system"""
        # Test that we can create formatted output
        test_panel = Panel("Test output", title="Test")
        # Note: We don't actually print it during tests 