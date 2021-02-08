string = "park zoo parking car"

print(string.count('park'))     #'park'가 나온 횟수
print(string.find('park',0))    #0번째부터 park 찾음
print(string.rfind('park'))    #뒤에서부터 park 찾음
print(string.index('park'))    #앞에서부터 park 위치 찾음, 못 찾으면 에러
print(string.rindex('park'))    #뒤에서부터 park 위치 찾음, 못찾으면 에러

string = " space "
print(string.strip())   #문장 앞뒤의 공백 없앰
string = "!@!@space!!@@"
print(string.strip('!@'))   #문장 앞뒤의 !@을 사용해 만들수있는 조합 없앰

longString = '''line1
line2
line3'''
lst = longString.splitlines()   #여려줄의 문자열을 개행문자 단위로 나눔
print('+'.join(lst))    #+와 리스트의 요소들을 더해서 문자열 만듬

print('one two three'.split(' ',1))     #문자열을 공백을 기준으로 한번만 나눔


