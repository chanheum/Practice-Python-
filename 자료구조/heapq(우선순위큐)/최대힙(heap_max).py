import heapq
def heap_sort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        # 단, 삽입할 때 부호를 -로 지정해서 넣어줘야한다.
        heapq.heappush(h, -value)

    # 힙에 삽입된 원소들을 차례대로 꺼내서 담기
    for i in range(len(h)):
        # heapq가 최소힙을 디폴트로 가져간다는 점에서 꺼낼 때 부호를 +로 바꿔주면 큰 수부터 꺼내는 효과를 낼 수 있다.
        result.append(-heapq.heappop(h))
    return result

result = heap_sort([1,3,5,7,9,2,4,6,8,0])
print(result)