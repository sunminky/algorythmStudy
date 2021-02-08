import sys
from math import sin

print(dir())    #현재 모듈에 정의된 이름 출력

print(sys.path) #모듈을 찾도록 지정된 폴더

## 문자열로 표현된 모듈 가져오기 ##
modulename = "re"
re = __import__(modulename)
print(re)

print(sys.modules)  #여태까지 호출되었던 모듈들 저장됨

print(sin.__module__)   #자신이 속한 모듈이름