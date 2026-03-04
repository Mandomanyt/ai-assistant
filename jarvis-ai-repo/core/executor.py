from modules.tools import run_terminal
from modules.search import web_search

def execute(step):
    step = step.lower()

    if "search" in step:
        return web_search(step.replace("search", ""))

    if "run" in step:
        return run_terminal(step.replace("run", ""))

    return "No tool executed"