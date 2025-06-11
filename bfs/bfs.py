from collections import deque


def bfs(graph):
    queue = deque()
    visited = []
    queue.extend(graph["you"])
    while queue:
        person = queue.popleft()
        if person not in visited:
            if person == "jonny":
                return f'Found {person}'
            queue.extend(graph[person])
            visited.append(person)
    return "Person not found"

def bfs_traversal(adj):
    queue = deque()
    path = []
    vertices_count = len(adj)

    visited = [False] * vertices_count
    queue.append(0)

    while queue:
        curr_vertex = queue.popleft()
        if not visited[curr_vertex]:
            path.append(curr_vertex)
            visited[curr_vertex] = True
            queue.extend(adj[curr_vertex])
    return path

def bfs_disconnected(adj):
    V = len(adj)
    
    # create an array to store the traversal
    res = []
    
    # Initially mark all the vertices as not visited
    visited = [False] * V
    
    # perform BFS for each node
    for i in range(V):
        if not visited[i]:
            bfs_traversal(adj, i, visited, res)
    return res

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

adj = [[1,2], [0,2,3], [0,1,4], [1,4], [2,3]]
adj = [[1, 2], [0], [0],
        [4], [3, 5], [4]]
print(bfs(graph))
# print(bfs_disconnected(adj))