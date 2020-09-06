#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    cage = [[] for _ in range(len(board))]  #인형이 쌓여질 공간(인형기계)
    result = [] #뽑은 인형을 저장할 배열
    wasteCnt = 0    #사라진 인형의 개수

    #인형뽑기 배열 세팅
    for seq1, rows in enumerate(board):
        for seq2, cols in enumerate(rows):
            if cols:    #0이 아닐경우 인형기계에 집어넣음
                cage[seq2].insert(0, cols)

    #인형 뽑기
    for posiotion in moves:
        if cage[posiotion-1]:   #뽑을수 있는 인형이 남은 경우
            poped = cage[posiotion-1].pop()
            # 같으면 터트리기 작업
            if result and poped == result[-1]:  #result가 비어있지 않고 새로 집어넣은 아이템이 result 가장위의 아이템과 같을 경우
                result.pop()    #result에서 가장 위 아이템을 삭제
                wasteCnt += 2   #사라진 인형의 개수 2개 증가
            else:
                result.append(poped)    #뽑은 인형을 result에 넣음

    return wasteCnt

if __name__ == '__main__':
    result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
    print(result)