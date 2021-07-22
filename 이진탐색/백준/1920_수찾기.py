from bisect import bisect_left, bisect_right
import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
# 이진 탐색을 위한 오름차순 정렬
data.sort()
m = int(sys.stdin.readline())
search = list(map(int, sys.stdin.readline().split()))

def data_search(array, target):
    bisect_r_index = bisect_right(array, target)
    bisect_l_index = bisect_left(array, target)
    result = bisect_r_index - bisect_l_index

    if result > 0:
        return 1
    else:
        return 0

for i in search:
    print(data_search(data, i))