import sys
T = int(sys.stdin.readline())

for _ in range(T):
    # 문자열 입력을 받을 때 마지막 엔터까지 들어가게 되지 않도록 해줘야함.
    inp = sys.stdin.readline().replace('\n','')
    # ()가 없어질 때가지 소거
    while inp.count('()'):
        inp = inp.replace('()', '')

    # 소거를 했는데도 남아있다면 완전히 VPS가 아님
    if len(inp) > 0:
        print("NO")
    else:
        print("YES")