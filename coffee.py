import os
import Coffee

coffee = 10
maxmoney = 10000
pay = 300

while True:
    # 현재 자판기에 남은 커피
    print('남은 커피 수: %d ' % coffee)
    # 현재 자판기에 남은 금액
    print('남은 금액: %d ' % maxmoney)

    print("##############################")
    money = int(input("돈을 넣어주세요: " ))
    num1 = int(input("몇개를 사시겠습니까?: " ))
    print("##############################")

    # 총 결제 금액
    endpay = pay * num1
    #거스름돈
    retrunpay = money - endpay


# 부족한 경우
    if money < 300:
        print("돈이 부족합니다")
        print("거스름돈은 %d 입니다" % money)
        continue
# 딱 맞는 경우
    elif money == 300:
        print("커피를 줍니다")
        print("거스름돈은 %d 입니다" % retrunpay)
        coffee -= num1
        maxmoney -= endpay

# 많은 경우
    elif money > 300:
        print("커피를 %d개 줍니다" % num1)
        print("거스름돈은 %d 입니다" % retrunpay)
# 거스름돈이 부족한 경우
        coffee -= num1
        maxmoney -= endpay
    # 넣은 돈에 비해 갯수가 많은경우
    elif endpay > money:
        print("갯수와 가격이 이상합니다.")
        print("거스름돈은 %d 입니다" % money)
        continue
# 매진인 경우
    if not coffee:
        print("***************************")
        print("커피 매진")
        print("***************************")
        break

