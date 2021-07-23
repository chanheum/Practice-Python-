n = int(input())
data = list(map(int, input().split()))
# 최저값을 나타내기 위한 오름차순 정렬
data.sort()

def cal(data):
    result = 0
    for i in range(len(data)):
        for j in range(i + 1):
            result += data[j]
    return result

print(cal(data))