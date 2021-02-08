a = 2
b = 3

c = eval('a+b') #식을 수행함, c = a+b 같은 문은 실행 불가
print(c)

exec('c = a**b') #문을 실행
print(c)

s = '''c = a + b
if c > 0:
    print(c,"는 0보다 큼")''' #여러줄의 문도 실행가능
exec(s)

result = compile(s,'<string>','exec')   #문 , 문자열이 저장된 파일이름(파일이 아니면 string), 여러줄이면 exec 한줄이면 single
#compile은 문을 컴파일 코드로 변환하고 다음부터는 컴파일 코드를 사용
exec(result)

result = compile("c = a ** b","<string>","single")
exec(result)    #저장된 문 실행
print(c)

src = open("Chapter1_1.py").read()  #파일 읽기
result = compile(src,"Chapter1_1.py",'exec') #오픈한 파일, 파일이름, 모드
exec(result)