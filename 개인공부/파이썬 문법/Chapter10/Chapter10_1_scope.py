def outer():
    x = 1

    def inner():
        nonlocal x  # 중첨된 함수의 변수를 사용, 가장가까운 이름공간의 변수 사용
        x += 2
        print(f"inner : {x}")

    inner()
    print(f"outer : {x}")


outer()  # inner : 3
# outer : 3
