# 연산

import sys
sys.stdin = open("sample_input.txt", "r")


def solve(lst):
    cnt = 0
    v = [False] * 1000001
    while True:
        temp = []
        for i in range(len(lst)):
            num = lst.pop()
            if num == m:
                return cnt
            else:
                t = num + 1
                if t <= 1000000 and not v[t]:
                    v[t] = True
                    temp.append(t)
                t = num - 1
                if t >= 1 and not v[t]:
                    v[t] = True
                    temp.append(t)
                t = num * 2
                if t <= 1000000 and not v[t]:
                    v[t] = True
                    temp.append(t)
                t = num - 10
                if t >= 1 and not v[t]:
                    v[t] = True
                    temp.append(t)
        cnt += 1
        lst = temp


T = int(input())
for tc in range(1, T+1):
    ans = 0
    n, m = map(int, input().split())
    arr = [n]

    ans = solve(arr)

    print(f'#{tc} {ans}')