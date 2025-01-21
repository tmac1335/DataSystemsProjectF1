from flask import Flask, jsonify, request
from baseline import construct_sparql_query, construct_sparql_queries
from pipeline import extract_ontology_description
from rdflib.plugins.sparql import prepareQuery
from rdflib import Graph
from flask_cors import CORS
# Create a Flask application
app = Flask(__name__)
CORS(app)
# Define a route for the API
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/query', methods=['POST'])
def query_db():
    # Check for valid JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Parse the JSON payload
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        # Parse the turtle file
        g = Graph()
        g.parse('../data/to_test.ttl', format="turtle")

        # Prepare and execute the query
        q = prepareQuery(query)
        results = g.query(q)

        # Format results as a JSON-serializable structure
        result_list = []
        for row in results:
            result_list.append({str(var): str(value) for var, value in row.asdict().items()})

        return jsonify({'result': result_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/', methods=['POST'])
def query_api():

    data = request.json
    query = data.get('query', 0)
    value = construct_sparql_queries(query)
    return jsonify({'result': value})
if __name__ == '__main__':
    app.run(port=5000)

    