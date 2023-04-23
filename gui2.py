import tkinter as tk
from tkinter import ttk
import pandas as pd
import json
import random

df = pd.read_csv("movies.csv")
result = []

def res(user_genre):
    row_count = df.shape[0]
    genre_col = df['genres']
    for i in range(row_count):
        row_dict = eval(genre_col.iloc[i])
        length = len(row_dict)
        for j in range(length):
            if row_dict[j]['name'] == user_genre:
                result.append(df['title'].iloc[i])
    return random.choice(result)

def on_submit():
    inpgenre = genre_entry.get()
    result_label.config(text=res(inpgenre))

root = tk.Tk()
root.title("Movie Recommender")

genre_label = ttk.Label(root, text="Enter the genre:")
genre_label.grid(row=0, column=0, padx=10, pady=10)

genre_entry = ttk.Entry(root)
genre_entry.grid(row=0, column=1, padx=10, pady=10)

year_label = ttk.Label(root, text="Enter the year:")
year_label.grid(row=1, column=0, padx=10, pady=10)

year_entry=ttk.Entry(root)
year_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()