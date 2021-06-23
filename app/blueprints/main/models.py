from flask_sqlalchemy import SQLAlchemy
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String, unique=True)
    title = db.Column(db.String)
    publisher = db.Column(db.String)

    def get_authors(self):
        return [a for a in Author.query.all() if a.book_id == self.book_id]

    def __repr__(self):
        return f'<Book: {self.book_id} | Title: {self.title} | Publisher: {self.publisher}>'

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    book_id = db.Column(db.String)

    def __repr__(self):
        return f'<Author: [{self.book_id}] {self.name}>'