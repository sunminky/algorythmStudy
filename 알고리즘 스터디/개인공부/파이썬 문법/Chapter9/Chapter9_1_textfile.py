#파일 쓰기
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\nLine 2")   #기록한 문자의 수 반환
    #f.close()  #with블록 안에서는 안해줘도 됨, 자동으로 해줌

#파일 쓰기
with open("test1.txt", "w", encoding="utf-8") as f:
    lines = ['Line 1\n', 'Line 2\n']
    f.writelines(lines) #여러 줄의 문장을 파일에 씀
    #f.close()  #with블록 안에서는 안해줘도 됨, 자동으로 해줌
    
#파일 읽기
with open("test.txt", "r", encoding="utf-8") as f:  #인코딩을 지정해서 저장했으면 읽을때도 인코딩 지정해서 읽어야 함
    print(f.read()) #파일전체 내용 읽음
    
#파일 읽기
with open("test1.txt", "r", encoding="utf-8") as f:  #인코딩을 지정해서 저장했으면 읽을때도 인코딩 지정해서 읽어야 함
    print(f.readlines()) #줄 단위로 여러 줄 읽어서 리스트에 저장

#파일 읽기
with open("test1.txt", "r", encoding="utf-8") as f:  #인코딩을 지정해서 저장했으면 읽을때도 인코딩 지정해서 읽어야 함
    line = f.readline() #한줄 읽음
    while line: #line이 ''이면 파일의 끝
        print(line)
        line = f.readline() #한줄 읽음