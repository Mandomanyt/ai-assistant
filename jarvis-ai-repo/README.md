# Jarvis AI Local Assistant

Features:
- Local AI using Ollama
- Desktop GUI
- Autonomous task planner
- Web search
- System command execution
- Memory storage

## Setup

1. Install Ollama and run:
   ollama pull mistral

2. Create virtual environment:
   python -m venv jarvis-env

3. Activate environment and install dependencies:
   pip install -r requirements.txt

4. Start Ollama:
   ollama serve

5. Run GUI:
   python gui.py