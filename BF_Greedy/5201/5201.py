# 컨테이너 운반

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 화물 무게
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    # 트럭 적재용량
    T = list(map(int, input().split()))
    T.sort(reverse=True)

    ans = 0
    for m in range(M):
        for n in range(N):
            if W[n] and W[n] <= T[m]:
                ans += W[n]
                W[n] = 0
                break

    print(f'#{tc} {ans}')