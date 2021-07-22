import heapq
# 무한대
INF = int(1e9)
# 노드의 개수, 간선의 개수 입력
n, m = map(int,input().split())
# 노드 간선정보 데이터
graph = [[] * (n + 1) for _ in range(n + 1)]
# 거리 정보 백업
distance = [INF] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
# 1에서 k를 거쳤다가 x로 가는 최단경로
print(distance[k] + distance[x])