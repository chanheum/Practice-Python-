from collections import deque

n, m = map(int, input().split())
visited = [[0] * (m) for _ in range(n)]
graph = []
# 북서남동
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for _ in range(n):
  graph.append(list(map(int,list(input()))))

def bfs(x, y):
  visited[x][y] = 1
  q = deque()
  q.append((x,y))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if graph[nx][ny] == 0 and visited[nx][ny] == 0:
          visited[nx][ny] = 1
          q.append((nx,ny))

result = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0 and visited[i][j] == 0:
      result += 1
      bfs(i, j)
print(visited)
print(result)