from flask import Flask, jsonify, render_template, request
import heapq

app = Flask(__name__)

# Network Topology Graph (Routers as nodes, Link latency/costs as weights)
network_graph = {
    'Router_A': {'Router_B': 4, 'Router_C': 2},
    'Router_B': {'Router_A': 4, 'Router_C': 1, 'Router_D': 5},
    'Router_C': {'Router_A': 2, 'Router_B': 1, 'Router_D': 8, 'Router_E': 10},
    'Router_D': {'Router_B': 5, 'Router_C': 8, 'Router_E': 2},
    'Router_E': {'Router_C': 10, 'Router_D': 2},
}


def dijkstra_shortest_path(graph, start, end):
  """Computes the shortest path and minimum transmission cost/latency

  using Dijkstra's Algorithm with a Priority Queue. Time Complexity: O(E log V)
  """
  distances = {node: float('inf') for node in graph}
  previous_nodes = {node: None for node in graph}
  distances[start] = 0
  priority_queue = [(0, start)]

  while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)

    # Ignore if a shorter path to this node has already been found
    if current_distance > distances[current_node]:
      continue

    if current_node == end:
      break

    for neighbor, weight in graph.get(current_node, {}).items():
      distance = current_distance + weight

      # Found a shorter path to the neighbor router
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        previous_nodes[neighbor] = current_node
        heapq.heappush(priority_queue, (distance, neighbor))

  # Reconstruct path from destination back to source
  path = []
  current = end
  while current is not None:
    path.append(current)
    current = previous_nodes[current]
  path.reverse()

  if distances[end] == float('inf'):
    return [], float('inf')

  return path, distances[end]


@app.route('/')
def index():
  return render_template('index.html', graph=network_graph)


@app.route('/api/route', methods=['POST'])
def calculate_route():
  data = request.json
  source = data.get('source')
  destination = data.get('destination')

  if (
      not source
      or not destination
      or source not in network_graph
      or destination not in network_graph
  ):
    return jsonify({'error': 'Invalid source or destination router'}), 400

  path, total_cost = dijkstra_shortest_path(network_graph, source, destination)
  return jsonify({'path': path, 'cost': total_cost, 'graph': network_graph})


if __name__ == '__main__':
  app.run(debug=True, port=5000)