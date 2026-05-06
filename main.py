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