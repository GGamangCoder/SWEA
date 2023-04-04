# dijksra(다익스트라) 알고리즘
# 최단 경로


V, E = map(int, input().split())
max_weight = 10

adj_matrix = [[max_weight+1] * (V+1) for _ in range(V+1)]

for i in range(E):
    start, end, weight = map(int, input().split())
    adj_matrix[start][end] = weight


def dijkstra(max_weight=10):
    distance = [max_weight * E] * (V+1)
    visited = [0] * (V+1)
    distance[0] = 0
    for _ in range(V):
        min_idx = -1
        min_value = max_weight * E
        # 최소 가중치 점 찾기 - 방문하지 않은 점 중 최소 비용 포인트
        for i in range(V + 1):
            if not visited[i] and min_value > distance[i]:
                min_idx = i
                min_value = distance[i]

        visited[min_idx] = 1

        for i in range(V + 1):
            if not visited[i] and distance[i] > distance[min_idx] + adj_matrix[min_idx][i]:
                distance[i] = distance[min_idx] + adj_matrix[min_idx][i]

    # 최종 점까지 도달하는데 걸리는 시간
    return distance[V]

print(dijkstra(10))