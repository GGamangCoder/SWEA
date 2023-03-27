# 최소합

import sys
sys.stdin = open("sample_input.txt", "r")


dir = [[-1, 0], [0, -1]]  # 방향, 왼쪽과 위에서
def function(idx):
    if idx > n*2 - 2:
        return

    if idx < n:
        for i in range(idx+1):
            # temp1 = graph[i+dir[0][0]][idx - i + dir[0][1]]
            # temp2 = graph[i+dir[1][0]][idx - i + dir[1][1]]
            temp = []
            for j in range(2):
                dx, dy = dir[j][0], dir[j][1]
                if 0 <= i + dx and 0 <= idx - i + dy:
                    temp.append(graph[i+dx][idx-i+dy])
            graph[i][idx-i] += min(temp)
    # idx >= n
    else:
        for i in range(n-1, idx-n, -1):
            temp = []
            for j in range(2):
                dx, dy = dir[j][0], dir[j][1]
                if 0 <= i + dx and 0 <= idx - i + dy:
                    temp.append(graph[i+dx][idx-i+dy])
            graph[i][idx-i] += min(temp)

    return function(idx+1)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    # (0,0) 다음 (0,1) 과 (1,0) 부터
    function(1)

    print(f'#{tc} {graph[-1][-1]}')