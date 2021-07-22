INF = int(1e9)
# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담기 위한 리스트
graph = [[] for _ in range(n + 1)]
# 방문한 적이 있는지 체크하기 위한 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한대로 먼저 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # 노드 a에서 b로 가기 위한 비용이 c라는 의미로 튜플 데이터 삽입
    graph[a].append((b,c))
    
# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드의 인덱스
    for i in range(1, n + 1):
        # 방문하지 않은 노드 중에서 최단경로인 노드
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
# 다익스트라 알고리즘 수행
def dijkstra(start):
    # 시작 노드에 대한 초기화
    distance[start] = 0
    visited[start] = True
    # 시작 노드에 연결된 노드들에 대한 경로 초기화
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해서 반복 탐색
    for _ in range(n - 1):
        # 현재 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드들의 거리를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[now]:
                distance[now] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])