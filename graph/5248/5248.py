# 그룹 나누기

import sys
sys.stdin = open("sample_input.txt", "r")


def union(x, y):
    i = find(x)
    j = find(y)
    if i > j:
        group[i] = j
    else:
        group[j] = i


def find(x):
    while x != group[x]:
        x = group[x]
    return x


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    group = [i for i in range(N+1)]

    for i in range(M):
        a, b = lst[2*i], lst[2*i+1]
        union(a, b)

    result = []
    for e in group:
        result.append(find(e))
    print(f'#{tc} {len(set(result))-1}')
