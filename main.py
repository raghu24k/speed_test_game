from tkinter import font
import pandas as pd
import tkinter as tk
import random 
import time

# sample Sentences
sentences = [
    'Python is powerfull programming language.',
    'Typing fast requires regular practice',
    'Artificial intelligence is changing the world',
    'coding imporves problem solving skills.'
]

start_time = 0

# start game
def start_game():
    global start_time

    sentence = random.choice(sentences)
    text_display.config(text=sentence)

    entry.delete(0,tk.END)

    result_label.config(text="")
    
    start_time = time.time()

# check typing
def check_typing():
    end_time = time.time()

    typed_text = entry.get()
    original_text = text_display.cget('text')

    time_taken = end_time - start_time

    word = len(typed_text.split())

    wpm = int((words/time_taken)*60)

    correct_chars = 0

    for i in range(min(len(typed_text),len(original_text))):
        if typed_text[i] == original_text[i]:
            correct_chars += 1

    accuracy = int((correct_chars/len(original_text)*100))
    result_label.config(
        text=f"WPM: {wpm} | Accuracy: {accuracy}"
    )

# main window
root = tk.Tk()
root.title("typing speed game")
root.geometry("700x400")

title = tk.Label(root,text="Typing speed tester", font=('Arial',24))
title.pack(pady=20)

text_display = tk.Label(
    root,
    text='Click start to Begin',
    wraplength=600,
    font= ('Arial',16)
)
text_display.pack(pady=20)

entry = tk.Entry(root,font=('Arial',16),width=50)
entry.pack(pady=20)
start_btn = tk.Button(
    root,
    text='start',
    font=('Arial',16),
    command=start_game
)