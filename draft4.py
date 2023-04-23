import pandas as pd
import json
import random
df=pd.read_excel("C:/Users/Neha Nirmal/Desktop/COLLEGE/PYTHON/Mini Project/moviessmall.csv.xlsx")

result=[]

def res(user_genre):
    row_count=df.shape[0]

    genre_col=df['genres']
    #year_col=df['release_date']
    #user_genre=input("Enter the genre:")
    #user_year=input("Enter the year:")
    for i in range(row_count):
        row_dict= eval(genre_col.iloc[i])
        """print(type(row_dict), row_dict)
        print(row_dict)"""
        length=len(row_dict)
        for j in range(length):
            if row_dict[j]['name']==user_genre:
                result.append(df['title'].iloc[i])
    print(random.choice(result))
inpgenre=input("Enter the genre:")        
res(inpgenre)