import subprocess
import appopener

def open_app(name):
    try:
        appopener.open(name)
        return f"Opening {name}"
    except:
        return "App not found"

def run_terminal(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout