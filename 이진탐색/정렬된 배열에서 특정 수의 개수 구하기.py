from bisect import bisect_left, bisect_right

n, x = map(int,input().split())
array = list(map(int, input().split()))

def count_on_list(array, target):
    left_index = bisect_left(array, target)
    right_index = bisect_right(array, target)
    return right_index - left_index

count = count_on_list(array, x)

if count == 0:
    print(-1)
else:
    print(count)