if __name__ =="__main__":
    inputData = input().split()
    coins = []
    cnt = 0

    coinvar = int(inputData[0])
    goal = int(inputData[1])

    for i in range(coinvar):
        coins.append(int(input()))

    coins.sort(reverse=True)

    for i, coin in enumerate(coins):
        cnt += goal // coin
        goal = goal % coin

    print(cnt)