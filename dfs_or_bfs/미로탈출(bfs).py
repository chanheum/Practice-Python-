from collections import deque
n, m = map(int,input().split())
# 0을 제외한 (1,1) 시작
graph = []
# 남동북서 탐색 좌표
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[0] * (m) for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 첫 노드부터 카운트하기 때문에 '1'로 시작
    visited[x][y] = 1
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        # 동서남북 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                # 방문한 적이 없으면서, 그래프 상으로 빈 공간이면 해당 노드로 가는 최단경로를 연산
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

bfs(0,0)
print(visited[n - 1][m - 1])