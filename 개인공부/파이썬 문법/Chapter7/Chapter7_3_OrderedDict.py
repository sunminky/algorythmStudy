### 순서를 유지하는 사전 ###
from _collections import OrderedDict
d = OrderedDict()
d['one'] = 1
d['two'] = 2
d['three'] = 3

print(d)    #데이터가 입력된 순서를 기억함, OrderedDict([('one', 1), ('two', 2), ('three', 3)])
d.popitem()     #맨 마지막 요소 꺼냄, ('three', 3)
d.move_to_end('one')    #('one', 1)을 맨 마지막으로 이동시킴
print(d)    #OrderedDict([('two', 2), ('one', 1)])