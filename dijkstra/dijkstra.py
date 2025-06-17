
def next_node(distances, processed):
    low_distance = float('inf')
    low_distance_node = -1
    for n in range(len(graph)):
        distance = distances[n]
        if distance < low_distance and n not in processed:
            low_distance = distance
            low_distance_node = n
    return low_distance_node

def dijkstra(graph):
    distances = [ d if d > 0 else float('inf') for d in graph[0] ]
    parents = [ 0 if d > 0 else -1 for d in graph[0] ]
    processed = []
    node = next_node(distances, processed)
    while node > 0:
        distance = distances[node]
        for n, distance in enumerate(graph[node]):
            if distance > -1:
                new_distance = distance + graph[node][n]
                if distances[n] > new_distance:
                    distances[n] = new_distance
                    parents[n] = node
        processed.append(node)
        node = next_node(distances, processed)
    
    return parents

def print_path(parents, index):
    if index < 0:
        return
    print_path(parents, parents[index])
    print(index)


vertices_number = 6
graph = [[-1 for _ in range(vertices_number)] for _ in range(vertices_number)]
graph[0][1] = 5
graph[0][2] = 2
graph[1][3] = 4
graph[1][4] = 2
graph[2][1] = 8
graph[2][4] = 7
graph[3][5] = 3
graph[4][5] = 1



distances = [float('inf')] * len(graph)
parents = dijkstra(graph)
print(parents)
print_path(parents, len(graph) - 1)