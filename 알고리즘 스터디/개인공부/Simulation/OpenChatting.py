# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    answer = []

    # uid 별 사용자 닉네임 얻기
    uid_table = dict()

    for txt in record:
        action, *data = txt.split()

        if action == "Leave":
            continue

        uid, nickname = data
        if action == "Change":
            uid_table[uid] = nickname
        else:

            uid_table[uid] = nickname

    for txt in record:
        action, *data = txt.split()

        if action == "Change":
            continue

        if action == "Enter":
            answer.append(f"{uid_table[data[0]]}님이 들어왔습니다.")
        else:
            answer.append(f"{uid_table[data[0]]}님이 나갔습니다.")

    return answer


if __name__ == '__main__':
    solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
    # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
