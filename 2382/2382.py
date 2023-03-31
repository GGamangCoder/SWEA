# 미생물 격리 - 시뮬, bfs


import sys
sys.stdin = open("sample_input.txt", "r")

def mix(lst):
    lst.sort()      # x, y, cnt, m 순으로 정렬될 것이므로
    idx = 0         # 현재 위치
    total = 0       # 한 영역 안에 총합 갯수
    new = []        # 새로 리턴할 리스트
    flag = False    # 마지막 인덱스 체크 요소
    cnt = len(lst)
    while idx < cnt-1:             # 이게 무슨 조건 ? idx < cnt -1
        total = temp_cnt = lst[idx][2]
        temp_dir = lst[idx][3]
        while idx < cnt-1:
            if lst[idx][0] == lst[idx+1][0] and lst[idx][1] == lst[idx+1][1]:
                temp2 = lst[idx+1][2]
                total += temp2
                if temp_cnt < temp2:
                    temp_dir = lst[idx+1][3]
                    temp_cnt = temp2
                idx += 1
                flag = True
            else:
                new.append((lst[idx][0], lst[idx][1], total, temp_dir))
                idx += 1
                flag = False
                break

    if flag == False:
        new.append((lst[idx][0], lst[idx][1], lst[idx][2], lst[idx][3]))
    else:
        new.append((lst[idx][0], lst[idx][1], total, temp_dir))

    return new


def move(lst):
    length = len(lst)
    new = []
    for _ in range(length):
        x, y, cnt, d = lst.pop()
        nx, ny = x + dir[d][0], y + dir[d][1]
        if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
            cnt = cnt // 2
            if cnt == 0:
                continue
            else:
                if d == '1':
                    d = '3'
                if d == '2':
                    d = '4'
                if d == '3':
                    d = '1'
                else:
                    d = '2'
        # 처리 끝나면 새롭게 초기화
        new.append((nx, ny, cnt, d))

    return mix(new)


T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    dir = {'1': (0, -1), '2': (0, 1), '3': (-1, 0), '4': (1, 0)}
    virus = []
    for _ in range(k):
        y, x, cnt, d = map(int, input().split())
        d = str(d)
        virus.append((x, y, cnt, d))

    # 움직이고, 합치고, 끝에 봐주고,
    for t in range(m):
        virus = move(virus)

    ans = 0
    for idx in virus:
        ans += idx[2]

    print(f'#{tc} {ans}')
