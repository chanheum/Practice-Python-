n, m = map(int, input().split())
visited = [[0] * (m) for _ in range(n)]
graph = []

# 북서남동
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for _ in range(n):
  graph.append(list(map(int,list(input()))))

# dfs 알고리즘 수행
def dfs(x, y):
    # 방문 처리
    visited[x][y] = 1
    # 동서남북 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 좌표 내에 있으면서 그래프에서 빈 공간이고, 방문한 적 없는 곳이면 dfs로 깊이 우선 탐색을 수행한다.
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                dfs(nx,ny)

result = 0
# 전체 그래프를 탐색하면서 탐색 조건이 되면 탐색을 수행한다.
for i in range(n):      # 0 - 3 (n)
    for j in range(m):  # 0 - 4 (m)
        if graph[i][j] == 0 and visited[i][j] == 0:
            result += 1
            dfs(i,j)

print(result)