fo = "1 + 2"

fo1 = str(fo)   #비형식적인 변환, 문자열을 보기좋게 바꿔줌
fo2 = repr(fo)  #형식적인 변환, 객체의 자료형을 정확하게 문자열로 표현

print(fo1)  #1 + 2
print(fo2)  #'1 + 2'
#print(eval(eval(fo1)))  #에러
print(eval(eval(fo2)))  #repr로 변환된 문자열은 eval로 다시 복구 가능

print(chr(97))  #a , 유니코드를 문자로 변환
print(ord('a'))  #97 , 문자를 유니코드로 변환

bstr = b"byteString"    #바이트
print(bstr.decode("utf-8"))    #byteString , 바이트에서 문자열로 변환
sstr = "stringstring"
print(sstr.encode("utf-8")) #b'stringstring' , 문자열에서 바이트로 변환

##파이썬 -> C언어 자료형 변환##
'''책 292쪽 ~ 298쪽 보기'''