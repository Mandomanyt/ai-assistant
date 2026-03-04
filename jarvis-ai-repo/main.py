from core.planner import create_plan
from core.executor import execute

print("Jarvis Autonomous AI Running")

while True:
    goal = input("Goal: ")
    steps = create_plan(goal)

    for step in steps:
        print("Step:", step)
        result = execute(step)
        print("Result:", result)