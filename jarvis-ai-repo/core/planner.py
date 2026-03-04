from core.brain import ask_ai

def create_plan(goal):
    prompt = f"Break this goal into steps: {goal}"
    result = ask_ai(prompt)
    return result.split("\n")