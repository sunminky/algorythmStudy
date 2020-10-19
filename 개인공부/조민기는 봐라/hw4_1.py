def dd():
    import math
    age = int(input("만 나이는?"))
    distance = int(input("이용거리?"))

    ##나이에 따른 이용거리##
    if age >= 13 and age <= 18: #청소년인 경우
        base = 720  #기본요금
        unit = 80   #추가요금
    elif age >= 6 and age < 13: #어린이인 경우
        base = 450  #기본요금
        unit = 50   #추가요금
    else:   #어른인경우
        base = 1250 #기본요금
        unit = 100  #추가요금

    fee = base  #기본요금 적용
    ##거리에 따른 운임##
    if distance < 10:   #10키로 미만
        fee = base  #기본요금만 냄
    elif distance >= 10 and distance < 50:  #10이상 50미만일 때
        fee += math.ceil((distance - 10) / 5) * unit    #기본요금 더하기 (50 - 10) * 추가요금
    elif distance >= 50:    #50키로 초과했을 때
        fee += (40 / 5 + math.ceil((distance - 50) / 8)) * unit #기본요금 + 40키로에 대한 추가요금 + 50키로 추가요금

    print("운임 :", fee)

if __name__ == '__main__':
    while True:
        dd()