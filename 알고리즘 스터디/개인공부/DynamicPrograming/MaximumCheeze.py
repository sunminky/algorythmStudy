arr = []

def eatCheeze(length):
    for i in range(1, length):
        for j in range(1, length):
            arr[i][j] += max(arr[i - 1][j], arr[i][j - 1])   #arr[x][y]는 반드시 arr[x-1][y]나 arr[x][y-1]을 지남
    return arr[length - 1][length - 1]

if __name__ == "__main__":
    length, cheezeNum = map(int, input("입력 : ").split())
    arr = [[0 for i in range(length)] for j in range(length)]

    for i in range(cheezeNum):  #치즈가 있는 자리라면 치즈 획득량 1증가
        y,x = map(int, input("좌표 : ").split())
        arr[x-1][y-1] += 1

    answer = eatCheeze(length)
    print(answer)
