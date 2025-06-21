import heapq


def dijkstra_with_none_init(graph, start_node):
    distances = {node: None for node in graph}
    distances[start_node] = 0

    previous_nodes = {node: None for node in graph}

    queue = [(0, start_node)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if (
            distances[current_node] is not None
            and current_distance > distances[current_node]
        ):
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if distances[neighbor] is None or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    return distances, previous_nodes


def reconstruct_path(previous_nodes, start_node, target_node):
    path = []
    current = target_node
    while current is not None:
        path.insert(0, current)
        if current == start_node:
            break
        current = previous_nodes.get(current)

    if path and path[0] == start_node:
        return path
    else:
        return []


server_network = {
    "Server_A": [("Server_B", 10), ("Server_C", 50)],
    "Server_B": [("Server_A", 10), ("Server_D", 30), ("Server_E", 70)],
    "Server_C": [("Server_A", 50), ("Server_D", 15)],
    "Server_D": [("Server_B", 30), ("Server_C", 15), ("Server_E", 20)],
    "Server_E": [("Server_B", 70), ("Server_D", 20), ("Server_F", 5)],
    "Server_F": [("Server_E", 5)],
}

start_server = "Server_A"
min_latencies, previous_servers = dijkstra_with_none_init(server_network, start_server)

print(f"Least delay (ping in ms) from '{start_server}':")
for server, latency in min_latencies.items():
    print(f"To {server}: {latency} ms")

print("\nFastest routes:")
for target_server in server_network:
    if target_server != start_server:
        path = reconstruct_path(previous_servers, start_server, target_server)
        if path:
            print(f"From {start_server} to {target_server}: {' -> '.join(path)}")
        else:
            print(f"From {start_server} to {target_server}: route not found.")
