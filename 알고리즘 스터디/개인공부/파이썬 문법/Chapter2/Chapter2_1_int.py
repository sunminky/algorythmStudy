print(isinstance(1,int))   #1이 정수인지 확인
n = 15
print(n.bit_length())      #n을 표현하는데 필요한 비트의 수
print(int('111',5))         #5진수 111을 10진수로 변환

n = -1
byteVar = n.to_bytes(2,byteorder='big',signed=True) #-1을 부호있는 2바이트 빅엔디안으로 변환
print(byteVar)

resoreVar = int.from_bytes(byteVar,byteorder='big',signed=True) #바이트를 정수로 변환
print(resoreVar)

resoreVar = int.from_bytes(b'\xff\xff',byteorder='big',signed=True) #위의 문장과 동일
print(resoreVar)

resoreVar = int.from_bytes([255,255],byteorder='big',signed=True) #위의 문장과 동일
print(resoreVar)