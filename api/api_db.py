import flask
from flask import request, jsonify
import sqlite3
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = flask.Flask(__name__)
app.config["Debug"] = True
app.config["JWT_SECRET_KEY"] = "secret"  # Change this!

jwt = JWTManager(app)

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def dict_factory(cursor, row):
    """Helper function to convert query results into a dictionary format"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
@limiter.limit("5 per day")
def home():
    """Homepage"""
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/login', methods=['POST'])
def login():
    """
    This endpoint authenticates a user and returns a JWT token.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Hardcoded user authentication (Replace with DB authentication)
    if username == "test" and password == "test":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    A protected route that requires authentication.
    """
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    """
    Fetch all books from the database.
    """
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    
    conn.close()  # Close the database connection
    return jsonify(all_books)

@app.errorhandler(404)
def page_not_found(error):
    """404 error handler"""
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    """
    Fetch books based on query parameters (id, published, author).
    """
    query_parameters = request.args

    book_id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if book_id:
        query += ' id=? AND'
        to_filter.append(book_id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (book_id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    
    conn.close()  # Close the database connection
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
