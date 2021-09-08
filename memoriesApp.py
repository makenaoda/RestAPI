import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# some test data for now; moving to a relational database later
thoughts = [
    {'id': 0,
     'type': 'memory',
     'date': '2021/07/25',
     'description': 'Found an abandoned shopping cart outside Matt\'s apartment. Pushed him one block two and from Cane\'s at 12am.'},
    {'id': 1,
     'type': 'book',
     'date': '2021/01/09',
     'description': 'Stamped from the Beginning (Ibram X. Kendi)'},
    {'id': 2,
     'type': 'movie',
     'date': '2021/09/04',
     'description': 'My Dinner with Andre'},
    {'id': 3,
     'type': 'memory',
     'date': '2021/04/01',
     'description': 'Nicole bought a heart-shaped swimming pool on a whim. We strapped it to the top of her car and sat in it at the beach, eating and talking. '}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Random Memory Archive</h1><p>This website is a compilation of random memories, and book, movie, and food recommendations.</p>"

@app.route('/memoriesApp/v1/resources/thoughts/all', methods=['GET'])
def api_all():
    return jsonify(thoughts)

@app.route('/api/v1/resources/thoughts', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for thought in thoughts:
        if thought['id'] == id:
            results.append(thought)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

# returns only 'memory' type objects
@app.route('/api/v1/resources/thoughts/memories', methods=['GET'])
def memories_all():
    results = []
    for thought in thoughts:
        if 'type' in request.args == 'memory':
            results.append(thought)

    return jsonify(results)

app.run()