#https://programmers.co.kr/learn/courses/30/lessons/64063

import timeit

def solution(k, room_number):
    rooms = {}
    answer = []
    answerAppend = answer.append

    for tenant in room_number:
        check_in_available = rooms.get(tenant, 0)
        if check_in_available == 0:
            # 방이 사용가능
            if rooms.get(tenant + 1, 0) != 0:
                # 바로 다음방이 비어있지 않다면
                rooms[tenant] = rooms.get(tenant + 1, 0)
            else:
                # 바로 다음방이 비어있다면
                rooms[tenant] = tenant+1
            answerAppend(tenant)
            
        else:
            invitedRooms = [tenant] #여태까지 비었는지 조사한 방
            invitedRoomsAppend = invitedRooms.append
            # 방이 사용불가능, 빈 방 찾기
            while check_in_available != 0:
                invitedRoomsAppend(check_in_available)  # 조사한 방들 저장
                check_in_available = rooms.get(check_in_available, 0)    #조사해야할 방

                if check_in_available == 0:
                    # 방이 사용가능
                    if rooms.get(invitedRooms[-1] + 1, 0) != 0:
                        # 바로 다음방이 비어있지 않다면
                        rooms[invitedRooms[-1]] = rooms.get(invitedRooms[-1] + 1, 0)
                    else:
                        # 바로 다음방이 비어있다면
                        rooms[invitedRooms[-1]] = invitedRooms[-1] + 1

                    #조사한 방들의 부모노드 갱신
                    occupied = rooms[invitedRooms[-1]]
                    for footPrint in invitedRooms:
                        rooms[footPrint] = occupied

                    answerAppend(invitedRooms[-1])

    return answer

if __name__ == '__main__':
    start = timeit.default_timer()
    result = solution(10**20, [1 for _ in range(10**1)])
    end = timeit.default_timer()
    print("걸린시간 :", end - start)
    print(result)