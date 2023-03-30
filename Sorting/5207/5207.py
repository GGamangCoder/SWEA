# 이진 탐색


import sys
sys.stdin = open("sample_input.txt", "r")


def binary_search(lst, t):
    l, r = 0, N-1
    flag = -1           # 왼쪽이면 0, 오른쪽이면 1
    while l <= r:
        mid = (l+r) // 2
        if lst[mid] == t:
            return 1
        elif lst[mid] < t:
            if flag == 1:
                return 0
            l = mid + 1
            flag = 1
        else:
            if flag == 0:
                return 0
            r = mid - 1
            flag = 0
    return 0


T = int(input())
for tc in range(1, T+1):
    ans = 0
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    for i in B:     # M 번
        ans += binary_search(A, i)

    print(f'#{tc} {ans}')