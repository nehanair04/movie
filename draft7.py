import pandas as pd
import random
import tkinter as tk
from tkinter import ttk

df=pd.read_csv("C:\\Users\\Neha Nirmal\\Desktop\\Downloads\\moviesFinal.csv.csv")

result=[]
def filter_movies(user_genre, user_year):
        user_genre = list(map(lambda x: x.lower(), user_genre))
        result=[]
        #filter based on genre
        row_count=df.shape[0]
        genre_col=df['genres']
        for i in range(row_count):
            row_dict= eval(genre_col.iloc[i])
            length=len(row_dict)
            for j in range(length):
                if row_dict[j]['name'].lower() in user_genre:
                    result.append(df['title'].iloc[i])
        
        #filter based on release date
        result1=[]
        if user_year==0:
            result1=result
        else:
            df['release_date'] = pd.to_datetime(df['release_date'])
            df['year'] = df['release_date'].dt.year.astype('Int64')
            for title in result:
                
                ind= df.loc[df["title"] == title]
                i=ind.index.values[0]
                if df['year'].iloc[i] == user_year:
                    result1.append(title)
                
        
        #recommending movie with highest rating
        global highest_index
        highest_index=0
        global highest_rating
        highest_rating=0
        for title in result1:
            ind= df.loc[df["title"] == title]
            i=ind.index.values[0]
            vote_avg=df['vote_avg'].iloc[i]
            if vote_avg>highest_rating:
                highest_rating=vote_avg
                highest_index=i
        recommended_movie=df['title'].iloc[highest_index]


        if not result1:
            return 'test', 'code'  # replace this with whatever you want
        result1.remove(recommended_movie)
        
        if len(result1)>=3:
            fresult=random.sample(result1,3)
        else:
            fresult=result1



        return recommended_movie, fresult


def on_submit():
    inpgenre = genre_entry.get().split(sep=",")
    choice=year_entry.get()
    if choice=="":
        inpyear=0
    else:
        inpyear=float(choice)
    result_label.config(text=filter_movies(inpgenre,inpyear))  

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
print("We think", result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10), "would be perfect for you!")

#result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
# recommend, extra= filter_movies(inpgenre,inpyear)
#print("We think", result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10), "would be perfect for you!")
# print("You could also check out", extra)