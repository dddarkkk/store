

import random as rm

roll = rm.randint(0, 10)
money = 1000
i = 1
while 1:
    num = input("请输入一个整数，起始金额1000，每次猜错-100，金额为0时游戏结束\n可通过输入q或Q直接退出游戏\n")
    if num == 'q' or num == 'Q':
        print('已退出游戏')
        break
    try:
        num = int(num)
        if int(num) == roll:
            print('ok')
            break
        elif int(num) <= roll:
            money -= 100
            print('猜错了,数字过小，金额-100，当前金额', money, '\t当前已猜错次数', i)
            i += 1
        elif int(num) >= roll:
            money -= 100
            print('猜错了，数字过大，金额-100，当前金额', money, '\t当前已猜错次数', i)
            i += 1
        if money == 0:
            print('金额已为0，游戏结束')
            break
    except ValueError:
        print('输入的字符不合法，请重新输入一个整数')
