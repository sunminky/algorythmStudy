#https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    #[전화번호 길이, 전화번호, 길이별 해쉬값]를 번호 길이 순으로 정렬
    phone_nums = sorted([[len(phone), phone, dict()] for phone in phone_book], key=lambda x:(x[0], x[1]))

    for i in range(len(phone_nums)):
        for j in range(i, len(phone_nums)):
            #현재 전화번호의 길이보다 긴 전화번호의 딕셔너리에 현재 전화번호만큼의 길이의 해쉬값을 추가
            if not phone_nums[j][2].get(phone_nums[i][0], False):
                phone_nums[j][2][phone_nums[i][0]] = int(hash(phone_nums[j][1][:phone_nums[i][0]]))
            #자기 자신이 아니고 해쉬값이 일치한 경우
            if i != j and phone_nums[i][2][phone_nums[i][0]] == phone_nums[j][2][phone_nums[i][0]]:
                return False

    return True

if __name__ == '__main__':
    solution(["119", "97674223", "1195524421"]) #False
    solution(["123","456","789"])   #True
    solution(["12","123","1235","567","88"])    #False