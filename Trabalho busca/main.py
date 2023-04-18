from queue import Queue

graph = {
    5: [1, 2, 3, 4],
    1: [2, 5],
    2: [1, 5],
    3: [5],
    4: [5]
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def leastDistance(graph, source):
    Q = Queue()
    # create a dictionary with large distance(infinity) of each vertex from source
    distance = {k: 9999999 for k in graph.keys()}
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({source})
    while not Q.empty():
        vertex = Q.get()
        if vertex == source:
            distance[vertex] = 0
        for u in graph[vertex]:
            if u not in visited_vertices:
                # update the distance
                if distance[u] > distance[vertex] + 1:
                    distance[u] = distance[vertex] + 1
                Q.put(u)
                visited_vertices.update({u})
    return distance


print("Distância:")
print(leastDistance(graph, 2))
print("--------------------------------")
print("Width Search:")
bfs(visited, graph, 2)
print("--------------------------------")
