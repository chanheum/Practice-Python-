# 로프 개수
k = int(input())
data = []
result = []
for _ in range(k):
    data.append(int(input()))
data.sort(reverse=True)

for num in range(k):
    result.append(data[num] * (num + 1))

print(max(result))