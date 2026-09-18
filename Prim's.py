V = int(input("Enter number of vertices: "))

graph = []

print("Enter matrix row by row :")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

parent = [-1] * V
key = [float('inf')] * V
inMST = [False] * V

key[0] = 0

for count in range(V - 1):
    
    minimum = float('inf')
    u = -1
    for i in range(V):
        if not inMST[i] and key[i] < minimum:
            minimum = key[i]
            u = i
            
    inMST[u] = True
    
    for v in range(V):
        if graph[u][v] > 0 and not inMST[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

print("\nEdge \tWeight")
total_cost = 0
for i in range(1, V):
    print(f"{parent[i]} - {i} \t  {graph[i][parent[i]]}")
    total_cost += graph[i][parent[i]]

print("Total Cost:", total_cost)