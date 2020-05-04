#with는 두개의 관련된 연산들 사이에 필요한 작업수행
#파일 열기 - 파일 닫기 같은 작업을 자동으로 처리함

with open("out.txt","r") as f:
    print(f.read())

#위의 코드와 동일한 작업
f = open("out.txt","r")
print(f.read())
f.close()