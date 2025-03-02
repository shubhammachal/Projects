import flask
from flask import request, jsonify 
import sqlite3
app = flask.Flask(__name__)
app.config["Debug"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> Distant reading archive</h1><p> This site is a prototype API for distant reading of science fiction novels.</p>"


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/api/v1/resources/books/all', methods = ['GET'])
def api_all():
    return flask.jsonify(books)

@app.route('/api/v1/resources/books', methods =['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
    return flask.jsonify(results)
        






if __name__ == '__main__':
    app.run(debug = True)