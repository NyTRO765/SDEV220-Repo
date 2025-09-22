"""
Module 4 Lab - Case Study - Python APIs

Author: Tre'tin Alvarez
Description: This script is to create a a CRUD API for a Book. The Book Model has the following parameters: id, book_name, author, and publisher.
"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Book('{self.book_name}', '{self.author}', '{self.publisher}')"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    
    return {"books": output}

app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher}

app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    if drink is None:
        return {"error": "Book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted"}
