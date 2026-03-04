import tkinter as tk
from core.brain import ask_ai

def send():
    user = entry.get()
    response = ask_ai(user)

    chat.insert(tk.END, "You: " + user + "\n")
    chat.insert(tk.END, "Jarvis: " + response + "\n\n")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Jarvis AI Assistant")

chat = tk.Text(root, height=25, width=70)
chat.pack()

entry = tk.Entry(root, width=60)
entry.pack()

btn = tk.Button(root, text="Send", command=send)
btn.pack()

root.mainloop()