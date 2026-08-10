from collections import deque

Graph = {
    0: [1, 3],
    1: [2],
    2: [4, 5],
    3: [4],
    4: [],
    5: []
}

def checkDAG(Graph):
    indegree = [0] * len(Graph)

    for i in Graph:
        for j in Graph[i]:
            indegree[j] += 1

    queue = deque()

    for i in range(len(Graph)):
        if indegree[i] == 0:
            queue.append(i)

    count = 0

    while queue:
        node = queue.popleft()
        count += 1

        for neighbor in Graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if count == len(Graph):
        return True
    else:
        return False


if checkDAG(Graph):
    print("Topological Sort is possible")

    indegree = [0] * len(Graph)

    for i in Graph:
        for j in Graph[i]:
            indegree[j] += 1

    queue = deque()

    for i in range(len(Graph)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in Graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)


else:
    print("Topological Sort is not possible")
print()
