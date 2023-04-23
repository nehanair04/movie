import pandas as pd
import random
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tkFont

df=pd.read_csv("C:\\Users\\Neha Nirmal\\Desktop\\Downloads\\moviesFinal.csv.csv")
def filter_movies(user_genre, user_year):
    result=[]
    #filter based on genre

    row_count=df.shape[0]
    genre_col=df['genres']
    for i in range(row_count):
        row_dict= eval(genre_col.iloc[i])
        length=len(row_dict)
        for j in range(length):
            if row_dict[j]['name'] in user_genre:
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

    if result1==[]:
        return random.sample(result,3)  # replace this with whatever you want
    else:    
        result1.remove(recommended_movie)
        
        if len(result1)>=3:
            fresult=random.sample(result1,3)
        else:
            fresult=result1  
    # print(recommended_movie,fresult)
    return recommended_movie, fresult


def on_submit():

    helv16 = tkFont.Font(family='Helvetica', size=16, weight='bold')
    monst14=tkFont.Font(family="Monstserrat", size=14, weight='bold')
    name = entry.get()
    
    new_window = tk.Toplevel(root)
    new_window.wm_title(f"Welcome, {name}")
    new_window.configure(bg = 'pink')

    style = Style() 
    style.configure('TButton',font =('Verdana', 12, 'bold'), foreground = 'blue', background = 'pink')

    label = Label(new_window, text=f"Welcome, {name}!", font= helv16, background = 'cyan')
    label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
    
    
    genre_label = Label(new_window, text="Enter the genre/genres:", font=helv16, background= 'cyan')
    genre_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)

    genre_list=['Action', 'Animation', 'Western', 'Adventure', 'Mystery', 'Family', 'Crime', 'War', 
    'Science Fiction', 'Drama', 'Horror', 'Romance', 'History', 'Thriller', 'Comedy', 'Music', 'Fantasy']
    value_inside = tk.StringVar(value=genre_list)
    genre_entry=tk.Listbox(new_window,listvariable=value_inside,selectmode="multiple", background= 'turquoise')
    genre_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.NSEW)

    year_label = Label(new_window, text="Enter the year(if you wish):", font=helv16, background= 'cyan')
    year_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)

    year_entry= Entry(new_window, background= 'turquoise')
    year_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)

    """new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_rowconfigure(0, weight=1)"""

    def on_submit():
        selected_options= genre_entry.curselection()
        inpgenre=[genre_list[i] for i in selected_options]
        choice=year_entry.get()
        if choice=="":
            inpyear=0
        else:
            inpyear=float(choice)
        x = filter_movies(inpgenre,inpyear)
        s = f"We think {x[0]} would be perfect for you!\nYou can also check out:"
        for i in x[1]:
            if len(s) > 30:
                s+="\n"
            s += f"{i}, "
        result_label.config(text=s)
        

    submit_button = Button(new_window, text="Submit", command=on_submit, style = 'TButton')
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

    result_label = Label(new_window, text="", background = 'turquoise', font = monst14)
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root = tk.Tk()
root.wm_title("CineMatch")
root.configure(bg = 'light blue')

label1 = tk.Label(root, text="Hi! This is CineMatch", bg = 'pink', font = 'verdana')
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = tk.Label(root, text="Please enter your name:", bg = 'pink', font = 'verdana')
label2.grid(row=1, column=0, padx=10, pady=10)
entry = tk.Entry(root, bg = 'turquoise')
entry.grid(row=2, column=0, padx=10, pady=10)
submit_button = tk.Button(root, text="Submit", command=on_submit, bg = 'pink')
submit_button.grid(row=3, column=0, padx=10, pady=10)
root.mainloop()