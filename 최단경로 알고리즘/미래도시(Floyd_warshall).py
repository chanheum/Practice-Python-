INF = int(1e9)
# 노드의 개수, 간선의 개수 입력
n, m = map(int,input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(n):
    for b in range(n):
        graph[a][b] = 0

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

x, k = map(int,input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], (graph[a][k] + graph[k][b]))

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)