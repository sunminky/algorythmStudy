#https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
def solution(land):
    maxValue = [[i for i in land[0]]]   #맨 첫줄은 자신의 값이 획득할수 있는 값의 최대임
    maxValue.extend([[0 for _ in range(4)] for _ in range(len(land)-1)])

    for i in range(1,len(land)):
        maxValue[i][0] = max(maxValue[i-1][1:4]) + land[i][0]   #바로 윗칸을 제외한 이전 줄에서의 최대값과 현재값을 더함
        maxValue[i][1] = max(maxValue[i-1][0:1] + maxValue[i-1][2:4]) + land[i][1]  #바로 윗칸을 제외한 이전 줄에서의 최대값과 현재값을 더함
        maxValue[i][2] = max(maxValue[i-1][0:2] + maxValue[i-1][3:4]) + land[i][2]  #바로 윗칸을 제외한 이전 줄에서의 최대값과 현재값을 더함
        maxValue[i][3] = max(maxValue[i-1][0:3]) + land[i][3]   #바로 윗칸을 제외한 이전 줄에서의 최대값과 현재값을 더함

    print(max(maxValue[len(land)-1]))
    return max(maxValue[len(land) - 1])

if __name__ == '__main__':
    solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])