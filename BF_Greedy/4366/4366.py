# 정식이의 은행업무

def binVal(lst):
    ans = 0
    l = len(lst)
    idx = 0
    for i in range(l-1, -1, -1):
        ans += 2**idx * lst[i]
        idx += 1
    return ans


def triVal(lst):
    ans = 0
    l = len(lst)
    idx = 0
    for i in range(l-1, -1, -1):
        ans += 3**idx * lst[i]
        idx += 1
    return ans


T = int(input())
for tc in range(1, T + 1):
    num1 = list(map(int, input()))
    num2 = list(map(int, input()))
    l1 = len(num1)
    l2 = len(num2)
    ans = 0
    for i in range(l1):
        num1[i] = int(not num1[i])      # 바꿔줬다가 테스트 후 뒤에서 다시 바꾸기
        temp1 = binVal(num1)            # 변환값
        for j in range(l2):
            for _ in range(2):
                num2[j] = (num2[j] + 1) % 3
                temp2 = triVal(num2)
                if temp1 == temp2:
                    ans = temp1
                    break
            num2[j] = (num2[j] + 1) % 3
        if ans:
            break
        num1[i] = int(not num1[i])

    print(f'#{tc} {ans}')
