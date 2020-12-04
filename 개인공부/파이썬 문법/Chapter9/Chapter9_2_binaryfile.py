import os

#이진파일 쓰기
with open("test.bin", "wb") as f:
    #f.write('stringData')  #이진파일에 문자열쓰기는 안됨
    f.write("stringData".encode())  #바이트형으로 변환해서 쓰기
    
#이진파일 읽기
with open("test.bin", "rb") as f:
    print(f.read(4).decode())    #3바이트만큼 읽은 데이터를 문자열로 바꿈
    print(f.readline()) #바이트로 읽음
    
#임의접근 파일
with open("test.bin", "rb") as f:
    f.seek(3, os.SEEK_CUR)   #현재부터 3번째 위치로 이동
    f.seek(-3, os.SEEK_END)  # 뒤에서 부터 -3번째 위치로 이동
    f.seek(2, os.SEEK_SET)  # 처음부터 2번째 위치로 이동
    print(f.tell()) #현재 위치 확인
    
#파일객체 속성
with open("test.bin", "rb") as f:
    print(f.closed) #파일의 닫힘 여부 확인
    print(f.mode)   #파일모드 확인
    print(f.name)   #파일이름