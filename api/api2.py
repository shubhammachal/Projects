from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import session, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"  
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Rate Limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Define Book Model (Matches Existing Database Schema)
class Book(db.Model):
    __tablename__ = "books"  # Ensure it matches your table name in books.db
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    published = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author, "published": self.published}

@app.route('/', methods=['GET'])
@limiter.limit("5 per day")
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args
    filters = {}

    if query_parameters.get("id"):
        filters["id"] = query_parameters.get("id")
    if query_parameters.get("published"):
        filters["published"] = query_parameters.get("published")
    if query_parameters.get("author"):
        filters["author"] = query_parameters.get("author")

    if not filters:
        return "<h1>404</h1><p>No filters provided.</p>", 404

    books = Book.query.filter_by(**filters).all()
    return jsonify([book.to_dict() for book in books])

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':
    app.run(debug=True)
