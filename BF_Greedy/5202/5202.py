# 화물 도크

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [tuple(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x: x[1])
    end = cnt = 0
    for t in time:
        if end <= t[0]:
            cnt += 1
            end = t[1]

    print(f'#{tc} {cnt}')