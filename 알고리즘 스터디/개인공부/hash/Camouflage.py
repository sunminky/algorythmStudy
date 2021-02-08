#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    closet = dict()
    answer = 1
    for item, category in clothes:  # 모든 옷에 대해서 탐색
        if category in closet:  # 이전에 카운트 한 카테고리인 경우
            closet[category] += 1
        else:  # 이전에 카운트하지 않은 카테고리인 경우
            closet[category] = 1

    for key in closet:  # 모든 카테고리에 대해서 탐색
        answer *= closet[key] + 1  # 카테고리 별 옷의 개수 + 옷을 안입는 경우

    return answer - 1  # 옷을 하나도 안입는 경우를 빼줌

if __name__ == '__main__':
    solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
    solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])