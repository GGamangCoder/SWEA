# 하나로


import sys
sys.stdin = open("re_sample_input.txt", "r")

maxV = 1000000000000
def prime():
    # 거리 누적
    distance = [maxV] * N
    distance[0] = 0
    # 방문 여부 체크
    visited = [0] * N
    total = 0
    for _ in range(N):
        min_idx = -1
        min_val = maxV * N
        for i in range(N):
            if not visited[i] and min_val > distance[i]:
                min_idx = i
                min_val = distance[i]

        visited[min_idx] = 1
        total += min_val * E

        for i in range(N):
            if not visited[i]:
                distance[i] = min(distance[i],
                              (X[min_idx]-X[i])**2 + (Y[min_idx]-Y[i])**2)

    return total

T = int(input())
for tc in range(1, T+1):
    # 섬의 갯수, N
    N = int(input())

    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    print('#{} {}'.format(tc, round(prime())))