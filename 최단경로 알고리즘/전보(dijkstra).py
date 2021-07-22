import heapq
# 무한대
INF = int(1e9)
# 도시(노드)의 개수, 통로(간선)의 개수, 메시지를 보내고자하는 도시(시작점) 입력
n, m, start = map(int, input().split())
# 각 노드들에 대한 간선 정보를 초기화할 데이터
graph = [[] for _ in range(n + 1)]
# 각 노드들에 대한 비용 정보 데이터
distance = [INF] * (n + 1)
for _ in range(m):
    # 노드 a에서 b로 가는데 걸리는 시간(비용)이 'c'
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    node_count = 0
    price_count = 0
    # 시작 노드에 대한 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드로 가는 비용이 이미 들어가 있는 비용보다 크면 이미 처리된 것으로 판단하여 무시한다.
        if dist > distance[now]:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인한다.
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으면 최단경로 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                node_count += 1
                price_count = max(price_count, distance[i[0]])

    return (node_count, price_count)

print(dijkstra(start))
# print(distance)