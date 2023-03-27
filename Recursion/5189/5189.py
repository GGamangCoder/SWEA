
import sys
sys.stdin = open("sample_input.txt", "r")


def find(x, sumValue):
    global minValue
    if 0 not in visited:
        if minValue > sumValue:
            minValue = sumValue
    elif minValue < sumValue:
        return
    for i in range(n):
        if i != x and not visited[i]:
            if i == 0 and 0 in visited[1:]:
                continue
            else:
                visited[i] = 1
                find(i, sumValue + graph[x][i])
                visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    minValue = sum(graph[0]) + sum(graph[1])
    visited = [0] * n
    find(0, 0)
    print(f'#{tc} {minValue}')
