import tkinter as tk
from tkinter import ttk

class MovieFilter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Movie Filter")
        self.geometry("500x500")

        # Create UI elements
        self.label_genre = ttk.Label(self, text="Genre:")
        self.combo_genre = ttk.Combobox(self, values=["Action", "Comedy", "Drama", "Horror", "Sci-Fi"])

        self.label_actor = ttk.Label(self, text="Actor:")
        self.entry_actor = ttk.Entry(self)

        self.label_director = ttk.Label(self, text="Director:")
        self.entry_director = ttk.Entry(self)

        self.label_year = ttk.Label(self, text="Year:")
        self.entry_year = ttk.Entry(self)

        self.button_filter = ttk.Button(self, text="Filter", command=self.filter_movies)

        self.tree_movies = ttk.Treeview(self, columns=("Title", "Genre", "Actor", "Director"))
        self.tree_movies.heading("#0", text="Title")
        self.tree_movies.heading("#1", text="Genre")
        self.tree_movies.heading("#2", text="Actor")
        self.tree_movies.heading("#3", text="Director")

        # Place UI elements on the window
        self.label_genre.grid(row=0, column=0)
        self.combo_genre.grid(row=0, column=1)

        self.label_actor.grid(row=1, column=0)
        self.entry_actor.grid(row=1, column=1)

        self.label_director.grid(row=2, column=0)
        self.entry_director.grid(row=2, column=1)

        self.label_year.grid(row=3, column=0)
        self.entry_year.grid(row=3, column=1)

        self.button_filter.grid(row=4, column=1)

        self.tree_movies.grid(row=5, column=0, columnspan=2)

    def filter_movies(self):
        genre = self.combo_genre.get()
        actor = self.entry_actor.get()
        director = self.entry_director.get()
        year = self.entry_year.get()

        # Perform filtering logic here
        # ...

        # Populate tree with filtered movies
        self.tree_movies.delete(*self.tree_movies.get_children())
        for movie in filtered_movies:
            self.tree_movies.insert("", "end", text=movie["Title"], values=(movie["Genre"], movie["Actor"], movie["Director"]))

if __name__ == "__main__":
    app = MovieFilter()
    app.mainloop()