#/*https://level.goorm.io/exam/49060/%EA%B0%9C%EB%AF%B8-%EC%A7%91%ED%95%A9%EC%9D%98-%EC%A7%80%EB%A6%84/quiz/1*/
import sys

if __name__ != "__main__" :
    exit()

N, D = input().split()
N = int(N)  #개미들의 개수
D = int(D)  #줄이고 싶은 반지름 수
ant = list(map(int, input().split()))   #개미들 위치 저장
min = sys.maxsize   #최소로 죽여야 하는 개미
killIndicator = 0   #개미를 앞에서 부터 어디까지 죽였는가 표시

# python2
#L = map(int, raw_input().split())

# python3
#ant = list(map(int, input().split()))
ant.sort()  #오름차순 정렬

if ant[N-1] - ant[0] <= D:  #이미 조건을 만족(현재 d보다 작음)하면 종료
    print(0)

else :
    for i in range(killIndicator, N):
        for j in range(i, N):
            if ant[j] - ant[i] <= D:    #현재 개미와 죽은 개미를 제외하고 제일 앞에 있는 개미와 거리 비교
                if min > N - j - 1 + i: #뒤에서 부터 죽인 개미 + 앞에서 부터 죽인 개미 < 최소값
                    min = N - j - 1 + i #최소값 갱신
            else:   #이 개미 뒤에있는 개미들은 조건을 만족하지 못함(d보다 큼)
                for k in range(killIndicator, j + 1):   #앞에서 개미를 얼마나 죽여야 d를 만족 할수 있는지 확인
                    if ant[j] - ant[k] <= D:
                        killIndicator = k
                        break
                if (N - j - 1 + i > min):   #오히려 죽어야 되는 개미의 수가 전보다 늘었다?? -> 최악효율 구간이군!
                    killIndicator = j   #최악의 효율구간은 빼야지
                break
    print(min)
