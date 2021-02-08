src = open("out.txt","w")   #파일을 쓰기모드로 열기
print("Write Text in File",file=src)    #인수 file을 사용하면 print로 파일에 쓰기 가능
src.close() #파일 닫기
print(open("out.txt").read())   #파일 내용 출력

print(format(1.234567,"10.2f")) #소수점 2째자리까지 10자리로 출력
print("{0:10.2f}".format(1.234567)) #위와 동일
print("{0} 과 {1}".format("앞","뒤"))

print("W" in 'World')   #World 안에 W가 들어있는지 여부 출력
print("W" not in 'World')   #World 안에 W가 안 들어있는지 여부 출력

bytevar = b"byteVar"    #바이트형으로 변수 선언
print(bytevar[::-1])    #역순으로 출력
bytevar.decode()    #바이트 변수를 문자열 변수로 변환
bytevar.decode("utf-8")    #바이트 변수를 문자열 변수로 변환
"stringVar".encode()    #문자열을 바이트로 변환

#bytevar[0] = ord('a')   #에러, 바이트는 변경불가능
bytearrayvar = bytearray(bytevar)
bytearrayvar[0] = ord('a')  #바이트어레이는 변경가능 ,ord()는 문자의 아스크코드값을 반환
