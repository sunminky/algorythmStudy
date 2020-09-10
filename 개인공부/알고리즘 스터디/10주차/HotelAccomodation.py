#https://programmers.co.kr/learn/courses/30/lessons/64063

def solution(k, room_number):
    rooms = [[i, False] for i in range(k+1)]   #그룹의 리더 저장
    answer = []
    
    for tenant in room_number:
        #방이 현재 사용가능한지 확인
        if not rooms[tenant-1][1]:
            #방이 사용가능
            occupied = rooms[tenant-1][0]
            rooms[tenant-1][1] = True
            rooms[tenant-1][0] = rooms[tenant][0]
        else:
            # 방이 현재 사용불가능
            loc = rooms[tenant-1][0]

            while rooms[loc][1]:
                loc = rooms[loc][0]

            occupied = loc
            rooms[loc][0] = rooms[loc + 1][0]
            rooms[loc][1] = True

        answer.append(occupied+1)

        '''else:
            #방이 현재 사용불가능
            occupied = rooms[rooms[tenant-1][0]][0]
            rooms[rooms[tenant-1][0]][1] = True
            rooms[rooms[tenant-1][0]][0] = rooms[rooms[tenant-1][0] + 1][0]

        answer.append(occupied + 1)
            
        ##리스트갱신##
        #아랫방 갱신
        for i in range(occupied-1, -1, -1):
            if not rooms[i][1]:
                break
            else:
                rooms[i][0] = rooms[i+1][0]'''

    print(answer)
    return answer

if __name__ == '__main__':
    solution(10, [1,1,1,1,1,1,1,1,1])