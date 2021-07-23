# 동전의 개수 및 만들고자하는 금액 k
n, k = map(int, input().split())
# 동전 단위를 입력할 리스트 변수
unit = []
# 동전 단위 입력
for _ in range(n):
    unit.append(int(input()))
    
# 단위가 높은 순부터 계산해야 하기 때문에 내림차순 정렬을 해준다.
unit.sort(reverse=True)
result = 0
num = k
# 단위가 높은 동전부터 카운트를 해준다.
for i in unit:
    if num // i > 0 or num % i == 0:
        result += (num // i)
        num -= (i * (num // i))
        if num == 0:
            break
    else:
        pass
print(result)