#!/usr/bin/env python3
"""
Stage 1 Demo: Project Setup and Environment
Building an Offline LLM Chatbot - Educational Series

This script demonstrates the foundation we're building in Stage 1:
- Project setup and configuration
- Basic class structure that will grow in future stages
- Environment verification and testing
- Foundation for the blog post content

Run this script to verify your Stage 1 setup is working correctly!

Usage:
    python main.py              # Run the basic demo
    python main.py --test       # Run system tests
    python main.py --status     # Show system status
"""

import sys
import argparse
from pathlib import Path

# Add src directory to Python path so we can import our modules
sys.path.append(str(Path(__file__).parent / "src"))

from chatbot_core import ChatbotCore
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


def main():
    """Main demonstration function for Stage 1."""
    
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description="Stage 1: Project Setup and Environment Demo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py              # Basic demo
  python main.py --test       # Run tests  
  python main.py --status     # Show status
  python main.py --config     # Show configuration
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
        "--quiet",
        action="store_true",
        help="Minimize output (useful for testing)"
    )
    
    args = parser.parse_args()
    
    # Initialize our console for rich output
    console = Console()
    
    # Create the chatbot core instance
    # Note: In Stage 1, this is simple. In later stages, this will:
    # - Load AI models (Stage 5)
    # - Initialize vector databases (Stage 4) 
    # - Set up document processors (Stage 2)
    # - Configure embeddings (Stage 3)
    # - And much more!
    
    if not args.quiet:
        console.print("\n🚀 [bold blue]Starting Stage 1 Demo...[/bold blue]\n")
    
    try:
        # Initialize the chatbot core
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
    Run the basic Stage 1 demonstration.
    
    This shows what we've built so far and prepares readers for what's coming.
    Perfect content for the blog post!
    """
    console = Console()
    
    # Show what we've accomplished in Stage 1
    demo_panel = Panel.fit(
        """
[bold green]🎉 Congratulations! Your Stage 1 setup is working perfectly![/bold green]

[bold]What we've built in Stage 1:[/bold]
✅ Solid Python project foundation
✅ Beautiful console output with Rich
✅ Configurable chatbot core class
✅ Extensible architecture for future stages
✅ Comprehensive testing framework
✅ Professional project structure

[bold yellow]💡 Key Learning Points:[/bold yellow]
• We're building incrementally - each stage adds new capabilities
• Good architecture makes complex systems manageable
• Testing early and often prevents problems later
• Clear documentation helps others (and future you!) understand the code

[bold blue]🔮 Coming in Stage 2:[/bold blue]
• Document processing (PDF, TXT, Markdown)
• Text chunking strategies  
• File handling and metadata
• Foundation for knowledge base building

[italic]Ready to continue? Stage 2 will build directly on what we have here![/italic]
        """,
        title="🤖 Stage 1 Complete!",
        border_style="green"
    )
    
    console.print(demo_panel)
    
    # Show current capabilities
    console.print("\n[bold]Current System Capabilities:[/bold]")
    capabilities = chatbot.get_capabilities()
    for i, capability in enumerate(capabilities, 1):
        console.print(f"  {i}. {capability}")
    
    # Give a preview of the architecture
    console.print("\n[bold]System Architecture Overview:[/bold]")
    architecture_table = Table(show_header=True, header_style="bold magenta")
    architecture_table.add_column("Component", style="cyan")
    architecture_table.add_column("Stage 1 Status", style="green")
    architecture_table.add_column("Future Enhancements", style="yellow")
    
    architecture_table.add_row(
        "ChatbotCore", 
        "✅ Basic structure", 
        "Will grow with each stage"
    )
    architecture_table.add_row(
        "Configuration", 
        "✅ Basic config system", 
        "Model settings, DB config, etc."
    )
    architecture_table.add_row(
        "Testing", 
        "✅ Test framework", 
        "Component-specific tests"
    )
    architecture_table.add_row(
        "Document Processing", 
        "🔮 Coming in Stage 2", 
        "PDF, TXT, Markdown support"
    )
    architecture_table.add_row(
        "Embeddings", 
        "🔮 Coming in Stage 3", 
        "Semantic similarity"
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


def run_tests(chatbot: ChatbotCore):
    """Run comprehensive system tests."""
    console = Console()
    
    console.print("\n🧪 [bold]Running Comprehensive System Tests...[/bold]\n")
    
    # Run the chatbot's built-in tests
    tests_passed = chatbot.test_system()
    
    # Additional Stage 1 specific tests
    console.print("[yellow]Running additional Stage 1 tests...[/yellow]")
    
    try:
        # Test that we can import everything we need
        import rich
        import colorama
        console.print("   ✅ All required dependencies available")
        
        # Test the configuration system
        config = chatbot.config
        assert config["stage"] == 1
        console.print("   ✅ Configuration system working")
        
        # Test capabilities reporting
        capabilities = chatbot.get_capabilities()
        assert len(capabilities) > 0
        console.print("   ✅ Capabilities reporting working")
        
        console.print("\n✅ [bold green]All Stage 1 tests passed![/bold green]")
        
    except Exception as e:
        console.print(f"\n❌ [red]Stage 1 tests failed: {e}[/red]")
        tests_passed = False
    
    # Summary
    if tests_passed:
        console.print("\n🎉 [bold green]Your Stage 1 setup is perfect! Ready for Stage 2.[/bold green]")
    else:
        console.print("\n⚠️ [bold yellow]Some tests failed. Check your setup.[/bold yellow]")


def show_status(chatbot: ChatbotCore):
    """Display detailed system status."""
    console = Console()
    
    status = chatbot.get_status()
    
    status_panel = Panel.fit(
        f"""
[bold]System Status Report[/bold]

[bold blue]Basic Information:[/bold blue]
  • Stage: {status['stage']}
  • Initialized: {'✅ Yes' if status['initialized'] else '❌ No'}
  • Name: {status['config']['name']}
  • Version: {status['config']['version']}

[bold blue]Current Capabilities:[/bold blue]
{chr(10).join(f'  • {cap}' for cap in status['capabilities'])}

[bold blue]Configuration Keys:[/bold blue]
{chr(10).join(f'  • {key}' for key in status['config'].keys())}

[bold yellow]Next Steps:[/bold yellow]
  Ready to move to Stage 2: Document Processing!
        """,
        title="🔍 System Status",
        border_style="blue"
    )
    
    console.print(status_panel)


def show_configuration(chatbot: ChatbotCore):
    """Display current configuration in detail."""
    console = Console()
    
    config_table = Table(show_header=True, header_style="bold magenta")
    config_table.add_column("Setting", style="cyan")
    config_table.add_column("Value", style="green")
    config_table.add_column("Description", style="yellow")
    
    config = chatbot.config
    
    config_table.add_row("stage", str(config["stage"]), "Current stage number")
    config_table.add_row("name", config["name"], "Project name")
    config_table.add_row("version", config["version"], "Current version")
    config_table.add_row("debug", str(config["debug"]), "Debug mode enabled")
    
    console.print("\n[bold]Current Configuration:[/bold]")
    console.print(config_table)
    
    console.print("\n[italic yellow]Note: Configuration will expand significantly in later stages![/italic yellow]")


if __name__ == "__main__":
    main() 