from flask import Flask, request, jsonify
from graph import Graph
from dijkstra import dijkstra
from ast import literal_eval

app = Flask(__name__)

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

    return jsonify({'path': path})

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
    

