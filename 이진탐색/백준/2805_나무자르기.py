import sys
n, m = map(int, sys.stdin.readline().split())
namu = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(namu)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # 시간초과 해결
    total = sum([(i - mid) for i in namu if i > mid])

    # 시간초과 해결 전
    # for i in namu:
    #     if i > mid:
    #         total += i - mid

    if total < m:
        end = (mid - 1)
    else:
        result = mid
        start = (mid + 1)

print(result)