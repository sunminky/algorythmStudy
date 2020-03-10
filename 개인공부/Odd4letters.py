def dozenNotation(source):
    ret = 0
    while(source != 0):
        rest = source % 12
        source = source // 12
        ret = ret + rest
    return int(ret)

def hexNotation(source):
    sum = 0
    for i in range(2,len(source)):
        sum += int('0x'+source[i],16)
    return int(sum)

def decNotation(source):
    sum = 0
    while(source != 0):
        rest = source % 10
        source = source // 10
        sum += rest
    return int(sum)

for i in range(1000,10000):
    tmp = decNotation(i)
    if tmp == dozenNotation(i) and tmp == hexNotation(hex(i)) :
        print(i)
