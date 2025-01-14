from flask import Flask, jsonify, request
from baseline import construct_sparql_query

# Create a Flask application
app = Flask(__name__)

# Define a route for the API
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/', methods=['POST'])
def query_api():
    data = request.json
    query = data.get('query', 0)
    value = construct_sparql_query(query)
    print(value)
    return jsonify({'result': value})

if __name__ == '__main__':
    app.run(port=5000)