from flask import Flask, request, jsonify
from graph import Graph
from dijkstra import dijkstra
from ast import literal_eval

app = Flask(__name__)

# Handle CORS requests
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8000')
  response.headers.add('Access-Control-Allow-Headers', 'content-type')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


# Routes
@app.route('/api/find_path', methods=['POST'])
def find_path():
    request_body  = request.get_json()

    grid = generate_grid(request_body)

    algorithm = request_body['algorithm']

    if algorithm == 'dijkstra':
        _,_,path = dijkstra(grid)
    else:
        # Default to dijkstra's algorithm
        _,_,path = dijkstra(grid)

    response = jsonify({'path': path})
    
    return response

# Helper Functions
def generate_grid(request_body):
    return {
        'size': int(request_body['size']),
        'start': coord_to_tuple(request_body['start']),
        'end': coord_to_tuple(request_body['end']),
        'obstacles': map(coord_to_tuple, request_body['obstacles'])
    }

def coord_to_tuple(coord):
    return literal_eval(coord)
