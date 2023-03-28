# 둘이서 하는 베이비진 게임

def babygin(lst, turn):
    for idx in range(10):
        if lst[idx]:
            if lst[idx] == 3:
                return turn
            elif idx <= 7 and lst[idx+1] and lst[idx+2]:
                return turn
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    A = cards[0::2]     # 짝수 번째 카드
    B = cards[1::2]     # 홀수 번째 카드
    countA = [0] * 10   # 카드 갯수
    countB = [0] * 10   # 카드 갯수

    ans = 0
    for i in range(6):
        countA[A[i]] += 1
        countB[B[i]] += 1
        if i >= 2:
            ans = babygin(countA, 1)
            if ans:
                break
            ans = babygin(countB, 2)
            if ans:
                break

    print(f'#{tc} {ans}')