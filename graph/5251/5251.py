# 최소 이동 거리


import sys
sys.stdin = open("./sample_input.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[9999999]*(N+1) for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    dp = [0] + [9999999] * N

    for start in range(N+1):
        for end in range(N+1):
            if dp[start] + graph[start][end] < dp[end]:
                dp[end] = dp[start] + graph[start][end]

    print(f'#{tc} {dp[N]}')
