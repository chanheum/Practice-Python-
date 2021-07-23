n = int(input()) # 설탕

result = 0 # 봉지 수

while True:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += (n // 5) # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가

    if n < 0:
        print(-1) # while문이 거짓이 되면 -1 출력
        break
