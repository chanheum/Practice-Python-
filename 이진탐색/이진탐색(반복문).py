# 이진 타색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스를 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우는 왼쪽을 확인한다.
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우는 오른쪽 을 확인한다.
        else:
            start = mid + 1
    # Target을 찾지 못했으면 None 반환
    return None

n, target = map(int, input().split())
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)