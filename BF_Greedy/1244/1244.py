# 최대 상금

T = int(input())
for tc in range(1, T + 1):
    temp, cnt = input().split()
    l = len(temp)
    current = set([temp])
    change = set()

    for _ in range(int(cnt)):
        while current:
            num = list(current.pop())
            for i in range(l):
                for j in range(i+1, l):
                    num[i], num[j] = num[j], num[i]
                    temp = ''.join(num)
                    change.add(temp)
                    num[i], num[j] = num[j], num[i]
        current, change = change, current

    print(f'#{tc} {max(current)}')


    # ans = temp      # 정답 저장 변수
    # for _ in range(cnt):
    #     for i in range(l):
    #         for j in range(i+1, l):
    #             num[i], num[j] = num[j], num[i]
    #             temp2 = ''.join(num)
    #             if temp < temp2:
    #                 temp = temp2
    #             num[i], num[j] = num[j], num[i]
    #
    #     if ans < temp:
    #         ans = temp
    #         num = list(ans)
    #     else:
    #         for i in range(10):
    #             if num.count(str(i)) > 1:
    #                 break
    #         else:
    #             num = list(ans)
    #             num[-1], num[-2] = num[-2], num[-1]
    #             ans = ''.join(num)

    # print(f'#{tc} {ans}')