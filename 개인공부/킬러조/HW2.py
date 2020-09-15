#180만원을 환전, 환율 1410.19, 5유로보다 적으면 원화로 거스름, (100,50,20,10,5) 단위
import math

if __name__ == '__main__':
    balance = 1800000   #내 잔고 180만원
    currency_rate = 1410.19 #환율
    currency_unit = [100, 50, 20, 10, 5]   #화폐단위
    total_currency = 0  #환전한 유로화의 총합
    euro = dict()   #화폐단위별 환전된 개수

    for unit in currency_unit:
        exchange = int(balance // (unit * currency_rate))   #화폐단위별로 환전
        total_currency += exchange * unit   #현재 환전된 금액을 현재까지 환전된 금액에 더함
        euro[unit] = exchange   #단위별로 환전된 개수 저장
        balance = balance % (unit * currency_rate)  #잔고에서 환전한 금액만큼을 제함

    balance = math.floor(balance)   #소수점 버림

    print("유로화 총액 : {tot} 거스름돈 : {bal}".format(tot=total_currency, bal=balance))

    for key in euro.keys():
        print("{unit}유로 : {num}".format(unit=str(key), num=str(euro[key])))