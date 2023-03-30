# 최소 생산 비용

import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(idx, res):
    global ans
    if idx == N:
        ans = min(ans, res)
        return

    if ans <= res:
        return

    for j in range(N):
        if not visited[j]:
            new_res = res + arr[idx][j]
            visited[j] = True
            dfs(idx+1, new_res)
            visited[j] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    ans = 1500
    dfs(0, 0)

    print(f'#{tc} {ans}')
