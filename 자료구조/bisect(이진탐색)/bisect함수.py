from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4
# bisect_left(array, x) : array 배열에서 x가 들어갈만한 좌측의 위치를 반환
print(bisect_left(a, x))
# bisect_right(array, x) : array 배열에서 x가 들어갈만한 우측의 위치를 반환
print(bisect_right(a, x))