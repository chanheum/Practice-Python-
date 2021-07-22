n, m = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # print('start = ', start, 'end = ', end, 'mid = ', mid)
    for x in array:
        if x > mid:
            # 잘랐을 때 떡의 양 계산
            total += (x - mid)

    # 떡의 양이 부족한 경우 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기서 Result에 기록
        start = mid + 1

print(result)