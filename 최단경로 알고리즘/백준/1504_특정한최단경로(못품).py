import heapq
# 무한대
INF = int(1e9)
# 노드의 개수, 간선의 개수
n, e = map(int, input().split())
# 각 노드에 대한 간선/비용 데이터 변수
graph = [[] for _ in range(n + 1)]
# 각 노드에 대한 최단경로 데이텨 변수
distance = [INF] * (n + 1)

for _ in range(e):
    a,b,c = map(int, input().split())
    # 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))
# 필수로 지나가야 하는 노드
v1, v2 = map(int,input().split())

def dijkstra(start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(1,0)
print(1,': ', distance)
distance = [INF] * (n + 1)
dijkstra(2,0)
print(2, ': ', distance)
distance = [INF] * (n + 1)
dijkstra(3,0)
print(3,': ', distance)
distance = [INF] * (n + 1)