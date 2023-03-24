def is_bipartite(graph):
    colors = [-1] * len(graph)
    colors[0] = 0
    stack = [0]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                colors[neighbor] = 1 - colors[node]
                stack.append(neighbor)
            elif colors[neighbor] == colors[node]:
                return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if is_bipartite(graph):
        print("B")
    else:
        print("N")
