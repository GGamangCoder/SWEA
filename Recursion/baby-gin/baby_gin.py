# Baby-Gin

import sys
sys.stdin = open("sample_input.txt", "r")


def check(lst):
    order = [0] * 10        # 숫자열
    cnt = num = 0
    for i in lst:
        order[i] += 1

    for i in range(10):
        while order[i] >= 3:
            cnt += 1
            order[i] -= 3
            num += 3
        while i <= 8 and order[i]:
            if order[i+1] and order[i+2]:
                order[i] -= 1
                order[i+1] -= 1
                order[i+2] -= 1

                cnt += 1
                num += 3
            else:
                num += 1
                break
        if cnt != 2 and num >= 4:
            return False
        elif cnt == 2:
            return True


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input()))
    print(f'#{tc} {int(check(cards))}')