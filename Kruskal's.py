def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v

        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u

        else:
            parent[root_v] = root_u
            rank[root_u] += 1

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
print("(Enter 0 if there is no edge)")

graph = []

for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    graph.append(row)

edges = []

for i in range(n):
    for j in range(i + 1, n):

        if graph[i][j] != 0:
            edges.append((i, j, graph[i][j]))

edges.sort(key=lambda x: x[2])

parent = []
rank = []

for i in range(n):
    parent.append(i)
    rank.append(0)

mst = []
total_cost = 0

for u, v, weight in edges:

    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:

        mst.append((u, v, weight))
        total_cost += weight

        union(parent, rank, u, v)

    if len(mst) == n - 1:
        break

print("\nEdges in Minimum Spanning Tree:")

for u, v, weight in mst:
    print(f"{u} - {v} = {weight}")

print("Minimum Cost =", total_cost)