import heapq
INF = int(1e9)
# 노드의 개수, 간선의 개수, 모이는 장소 초기화
n, m, x = map(int,input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
result = [0] * (n + 1)
# 간선 정보 입력
for _ in range(m):
    # 노드 a에서 b로 가는데 드는 시간 'c'
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
# start 지점에서 end 지점으로 가는데 걸리는 최단 경로를 반환
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

for i in range(1, n + 1):
    dijkstra(i)
    result[i] += distance[x]
    # print(i, ': ', distance)
    # 출발 노드가 'x'노드라면 돌아가는 것으로 간주하고 각 노드에 대한 돌아가는 시간비용을 더해준다.
    if i == x:
        for j in range(1, n + 1):
            result[j] += distance[j]
    distance = [INF] * (n + 1)

print(max(result))