# N: 원소의 갯수, M: 집합 정보 갯수

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 서로소 집합 표현을 위한 리스트
powerset = [0 for _ in range(N + 1)]
# powerset[i] 원소는 자신이 속한 집합에서 대표하는 원소를 나타낸다, 루트 원소

# 집합 초기화, Make-set, 자기 자신
for i in range(N+1):
    powerset[i] = i


####################################################
# Union - Find ()
# x 원소가 속한 집합의 대표 원소(루트)를 반환하는 함수
def find(x):
    # 자기 자신을 루트로 갖는 원소를 찾을 때까지,
    while x != powerset[x]:
        x = powerset[x]

    return x


# 두 개의 원소(x, y)가 속한 각각의 집합을 합 해준다.
def union(x, y):
    powerset[find(y)] = find(x)
####################################################


for i in range(M):
    union(arr[i * 2], arr[i * 2 + 1])


print(powerset)