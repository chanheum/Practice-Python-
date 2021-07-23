import heapq
# 회의의 수
n = int(input())
q = []
for _ in range(n):
    a,b = map(int, input().split())
    heapq.heappush(q, (a, b))
count = 0
pre_start = 0
pre_end = 0
while q:
    start, end = heapq.heappop(q)

    # 회의 시작시간이 0이면 무시
    if start == 0:
        continue
    # 시작시간이 이전과 같은 경우 무시 (이미 계산된 것으로 간주)
    if pre_start == start:
        continue
    # 이전에 확인했던 회의 시간이 다음 시간과 겹치는 경우 무시
    if start < pre_end:
        continue
    # 이전 회의시간 저장
    pre_start = start
    pre_end = end
    count += 1

print(count)