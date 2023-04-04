# 최소 이동 거리


import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())


    ans = 0
    print(f'#{tc} {ans}')
