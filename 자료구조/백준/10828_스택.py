import sys

q = int(sys.stdin.readline())
data = []
while q:
    q -= 1
    Input = list(sys.stdin.readline().split())

    if Input[0] == 'push':
        data.append(Input[1])
    elif Input[0] == 'top':
        if len(data) != 0:
            print(data[-1])
        else:
            print(-1)
    elif Input[0] == 'size':
        print(len(data))
    elif Input[0] == 'empty':
        if len(data) > 0:
            print(0)
        else:
            print(1)
    elif Input[0] == 'pop':
        if len(data) <= 0:
            print(-1)
        else:
            print(data.pop())

    # print(q)