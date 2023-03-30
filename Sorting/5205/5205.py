# 퀵 정렬


import sys
sys.stdin = open("sample_input.txt", "r")


def sort(lst, l, r):
    p = lst[l]
    i, j = l+1, r
    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    # 피벗을 갖다 껴넣기
    lst[j], lst[l] = lst[l], lst[j]
    return j

def quick(lst, l, r):
    if l < r:
        mid = sort(lst, l, r)
        quick(lst, l, mid - 1)
        quick(lst, mid + 1, r)


T = int(input())
for tc in range(1, T+1):
    ans = 0
    N = int(input())
    arr = list(map(int, input().split()))

    quick(arr, 0, N-1)

    print(f'#{tc} {arr[N//2]}')