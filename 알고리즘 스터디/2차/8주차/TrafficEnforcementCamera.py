def solution(routes):
    coverage = [-30000, 30000]  #카메라가 커버할수 있는 구역을 저장, 맨 처음 카메라는 -30000에 설치되었다고 가정
    numCameras = 1  #설치된 카메라의 개수

    routes.sort(key=lambda x: x[0])  #출발지점이 앞에있는 순서대로 정렬

    for head, tail in routes:
        # 카메라를 조금 뒤로 땡겨도 되는 경우
        if head > coverage[0]:
            coverage[0] = head
        # 카메라의 커버범위는 그 구역에서 가장 빨리나가는 운전자의 도착지까지임
        if tail <= coverage[1]:
            coverage[1] = tail
        # 새로운 카메라를 추가해야하는 경우
        if head > coverage[1]:  #현재 설치한 카메라로는 새로운 운전자를 커버할수 없다
            #카메라 추가설치
            numCameras += 1
            coverage[0] = head
            coverage[1] = tail

    return numCameras

if __name__ == '__main__':
    solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])