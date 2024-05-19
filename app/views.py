from flask import request, jsonify
from app import db
from app.models import Book, Author
from app import create_app

app = create_app()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book added"}), 201

@app.route('/categories/<category_type>', methods=['POST'])
def add_categories(category_type):
    data = request.get_json()
    if category_type == 'authors':
        for item in data:
            author = Author(name=item)
            db.session.add(author)
    # Add other categories similarly
    db.session.commit()
    return jsonify({"message": f"{category_type} added"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    epoch = request.args.get('epoch')
    genre = request.args.get('genre')
    author = request.args.get('author')
    query = Book.query
    if epoch:
        query = query.filter_by(epoch=epoch)
    if genre:
        query = query.filter_by(genre=genre)
    if author:
        query = query.join(Author).filter(Author.name == author)
    books = query.all()
    return jsonify([book.title for book in books])
