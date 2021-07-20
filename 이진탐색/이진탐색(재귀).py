# 이진 타색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    # start가 end보다 더 크면 target을 결국 찾지 못하고 탐색이 끝나버리는 상황이 됨.
    if start > end:
        return None

    mid = (start + end) // 2

    # mid값과 target 값이 같으면 찾은 것이므로 현재 위치를 출력한다.
    if array[mid] == target:
        return mid
    # mid값이 target 값보다 크면 우측은 버리고 좌측만 탐색한다.
    # 단, 좌측 탐색 시 mid에서 한 칸 앞까지로 범위를 지정한다.
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # mid값이 target 값보다 작으면 좌측은 버리고 우측만 탐색한다.
    # 단, 우측 탐색 시 mid보다 한 칸 뒤부터 탐색하도록 범위를 지정한다.
    else:
        return binary_search(array, target, mid + 1, end)

n, target = map(int, input().split())
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)