import random

n = 15  # number of rooms

# Create graph using adjacency matrix
graph = [[0 for _ in range(n)] for _ in range(n)]

# Generate random connections
for i in range(n):
    for j in range(i + 1, n):
        if random.randint(0, 1) == 1:  # 50% chance of connection
            weight = random.randint(1, 10)
            graph[i][j] = weight
            graph[j][i] = weight

# Dijkstra without heap
def dijkstra(graph, start):
    n = len(graph)
    dist = [9999] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        # Find minimum distance unvisited node
        min_dist = 9999
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        # Update distances
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    # Replace unreachable with -1
    for i in range(n):
        if dist[i] == 9999:
            dist[i] = -1

    return dist

# Run from entrance (room 0)
result = dijkstra(graph, 0)

# Print graph
print("Adjacency Matrix (Dungeon Map):")
for row in graph:
    print(row)

# Print shortest distances
print("\nShortest time from Room 0:")
for i in range(n):
    print("Room", i, "->", result[i])
