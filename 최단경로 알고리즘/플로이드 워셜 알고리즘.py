# 각 단계마다 특정한 노드 k를 거쳐가는 경우를 확인
# a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 탐색
# D_ab = min(D_ab, D_ak + D_kb)
# 단, O(N^3)의 시간복잡도를 갖고 있기 때문에 최소 노드가 500개 이상이면 안됨.
INF = int(1e9)
# 노드의 개수 및 간선의 개수 입력
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c라는 의미로 설정
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], (graph[a][k] + graph[k][b]))

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end = '')
        else:
            print(graph[a][b], end = '')
print()