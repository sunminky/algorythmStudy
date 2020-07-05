contest1Prize = (500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10)
contest2Prize = (512,256,256,128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32)

def winPrize(contest1, contest2):
    result = 0
    if contest1-1 < len(contest1Prize) and not contest1 == 0:   #대회1에서 얻을수 있는 상금
        result += contest1Prize[contest1-1]
    if contest2-1 < len(contest2Prize) and not contest2 == 0:   #대회2에서 얻을수 있는 상금
        result += contest2Prize[contest2-1]
    print(result*10000)

if __name__ == '__main__':
    loopCount = int(input())
    for i in range(loopCount):
        contest1, contest2 = map(int,input().split())
        winPrize(contest1, contest2)
