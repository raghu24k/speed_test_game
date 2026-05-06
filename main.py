import tkinter as tk
import random
import time

# Sample sentences
sentences = [
    "Python is a powerful programming language.",
    "Typing fast requires regular practice.",
    "Artificial intelligence is changing the world.",
    "Coding improves problem solving skills."
]

start_time = 0

# Start game
def start_game():
    global start_time

    sentence = random.choice(sentences)
    text_display.config(text=sentence)

    entry.delete(0, tk.END)

    result_label.config(text="")

    start_time = time.time()

# Check typing
def check_typing():
    end_time = time.time()

    typed_text = entry.get()
    original_text = text_display.cget("text")

    time_taken = end_time - start_time

    words = len(typed_text.split())

    wpm = int((words / time_taken) * 60)

    correct_chars = 0

    for i in range(min(len(typed_text), len(original_text))):
        if typed_text[i] == original_text[i]:
            correct_chars += 1

    accuracy = int((correct_chars / len(original_text)) * 100)

    result_label.config(
        text=f"WPM: {wpm} | Accuracy: {accuracy}%"
    )

# Main window
root = tk.Tk()
root.title("Typing Speed Game")
root.geometry("700x400")

title = tk.Label(root, text="Typing Speed Tester", font=("Arial", 24))
title.pack(pady=20)

text_display = tk.Label(
    root,
    text="Click Start to Begin",
    wraplength=600,
    font=("Arial", 16)
)
text_display.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16), width=50)
entry.pack(pady=20)

start_btn = tk.Button(
    root,
    text="Start",
    font=("Arial", 14),
    command=start_game
)
start_btn.pack(pady=10)

check_btn = tk.Button(
    root,
    text="Check Result",
    font=("Arial", 14),
    command=check_typing
)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

root.mainloop()