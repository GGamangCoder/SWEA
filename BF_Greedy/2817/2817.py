# 부분 수열의 합

import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(res, idx):
    global cnt
    if res > K:
        return
    elif res == K:
        cnt += 1
        return
    else:
        if idx == N:
            return

        dfs(res, idx+1)
        temp = res + lst[idx]
        if temp > K:
            return
        dfs(temp, idx+1)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    visited = [0] * N
    cnt = 0
    for i in range(N):
        dfs(0, i)

    print(f'#{tc} {cnt}')