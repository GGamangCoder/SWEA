# 동철이의 일 분배


import sys
sys.stdin = open("input.txt", "r")


def cal(i, res):
    global ans
    # 마지막 포인트
    if i == N:
        ans = max(ans, res)
        return
    # 가지치기
    if res <= ans:
        return

    for j in range(N):
        if not visited[j]:
            new_res = res * p[i][j]
            visited[j] = True
            cal(i+1, new_res)
            visited[j] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())            # 1 <= N <= 16
    p = [0] * N
    for i in range(N):
        p[i] = list(map(lambda x: int(x)/100, input().split()))

    ans = 0
    visited = [False] * N
    cal(0, 1)
    # for i in range(N):
    #     maxVal = p[i][0]
    #     maxidx = 0
    #     for j in range(N):
    #         val = p[i][j]
    #         if val > maxVal and not visited[j]:
    #             maxVal, maxidx = val, j
    #     visited[maxidx] = True
    #     ans *= maxVal
    ans = ans * 100

    print('#{} {:.6f}'.format(tc, ans))