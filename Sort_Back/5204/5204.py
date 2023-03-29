# 병합 정렬

import sys
sys.stdin = open("sample_input.txt", "r")


def sort(lst):
    leng = len(lst)
    if leng == 1:
        return lst

    mid = leng // 2
    left = sort(lst[:mid])
    right = sort(lst[mid:])
    return merge(left, right)


# 왼/오 둘 다 list
def merge(left, right):
    global ans

    # 문제 조건
    if left[-1] > right[-1]:
        ans += 1

    # 정렬
    merge_lst = []
    left_idx, right_idx = 0, 0
    len_left, len_right = len(left), len(right)

    while left_idx < len_left and right_idx < len_right:
        if left[left_idx] <= right[right_idx]:
            merge_lst.append(left[left_idx])
            left_idx += 1
        else:
            merge_lst.append(right[right_idx])
            right_idx += 1
    if left_idx != len_left:
        merge_lst += left[left_idx:]
    if right_idx != len_right:
        merge_lst += right[right_idx:]

    return merge_lst


T = int(input())
for tc in range(1, T+1):
    ans = 0
    N = int(input())
    arr = list(map(int, input().split()))
    arr = sort(arr)

    print(f'#{tc} {arr[N//2]} {ans}')