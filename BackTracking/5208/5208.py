# 전기버스2

import sys

sys.stdin = open("sample_input.txt", "r")


def dfs(idx, cnt):
    global ans
    if idx >= N:
        cnt -= 1
        ans = min(cnt, ans)
        return

    if cnt > ans:
        return

    pos = charge[idx]
    for i in range(pos, 0, -1):
        dfs(idx+i, cnt+1)


T = int(input())
for tc in range(1, T + 1):
    charge = list(map(int, input().split()))
    N = charge[0]

    ans = N
    dfs(1, 0)
    print(f'#{tc} {ans}')
