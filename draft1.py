import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget, QTableWidgetItem)

class MovieFilter(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        self.label_genre = QLabel("Genre:")
        self.combo_genre = QComboBox()
        self.combo_genre.addItems(["Action", "Comedy", "Drama", "Horror", "Sci-Fi"])

        self.label_actor = QLabel("Actor:")
        self.line_actor = QLineEdit()

        self.label_director = QLabel("Director:")
        self.line_director = QLineEdit()

        self.label_year = QLabel("Year:")
        self.line_year = QLineEdit()

        self.button_filter = QPushButton("Filter")
        self.button_filter.clicked.connect(self.filter_movies)

        self.table_movies = QTableWidget()
        self.table_movies.setColumnCount(4)
        self.table_movies.setHorizontalHeaderLabels(["Title", "Genre", "Actor", "Director"])

        # Create layouts
        h_layout_genre = QHBoxLayout()
        h_layout_genre.addWidget(self.label_genre)
        h_layout_genre.addWidget(self.combo_genre)

        h_layout_actor = QHBoxLayout()
        h_layout_actor.addWidget(self.label_actor)
        h_layout_actor.addWidget(self.line_actor)

        h_layout_director = QHBoxLayout()
        h_layout_director.addWidget(self.label_director)
        h_layout_director.addWidget(self.line_director)

        h_layout_year = QHBoxLayout()
        h_layout_year.addWidget(self.label_year)
        h_layout_year.addWidget(self.line_year)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_genre)
        v_layout.addLayout(h_layout_actor)
        v_layout.addLayout(h_layout_director)
        v_layout.addLayout(h_layout_year)
        v_layout.addWidget(self.button_filter)
        v_layout.addWidget(self.table_movies)

        self.setLayout(v_layout)

        self.setWindowTitle("Movie Filter")
        self.show()

    def filter_movies(self):
        genre = self.combo_genre.currentText()
        actor = self.line_actor.text()
        director = self.line_director.text()
        year = self.line_year.text()

        # Perform filtering logic here
        # ...

        # Populate table with filtered movies
        self.table_
