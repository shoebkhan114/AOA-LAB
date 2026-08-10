Graph = []
n = int(input("Enter NO. of Node:- "));
for i in range(n):
    ls = list(map(int,input().split()))
    Graph.append(ls)
INF = float("inf")
dist = [INF]*n
source = 0
visited = [False]*n
dist[source] = 0

for i in range(n):
    u = -1
    new_dist = INF
    for j in range(n):
        if not visited[j] and dist[j] < new_dist:
            new_dist = dist[j]
            u = j
    visited[u] = True

    for v in range(n):
        if Graph[u][v] != 0 and not visited[v]:
            if dist[u] + Graph[u][v] < dist[v]:
                dist[v] = dist[u] + Graph[u][v]
print("Shortest Distances:")
for i in range(n):
    print(i, "=", dist[i])            