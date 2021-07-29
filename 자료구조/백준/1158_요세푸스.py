from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
q = deque()
for i in range(1, n + 1):
    q.append(i)

print('<',end='')
for _ in range(n):
    for _ in range(m):
        # -1 :  반시계방향 회전
        q.rotate(-1)
    print(q.pop(),end='')
    if q:
        print(', ',end='')
    else:
        print('',end='')
print('>',end='')


