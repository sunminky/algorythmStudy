globals()   #전역영역의 심볼테이블 얻음

import math
math.__dict__['sin']    #이름공간에서 이름의 값을 얻어냄, <built-in function sin>
getattr(math,'sin')    #위와 동일, <built-in function sin>
setattr(math,'myData','950809') #이름공간에 값을 설정

### 자신의 모듈을 참조하기 ###
import sys
currentModule = sys.modules[__name__]
testData = 950809
currentModule.__dict__['testData']  #현재모듈의 testData의 값을 얻어옴, 950809