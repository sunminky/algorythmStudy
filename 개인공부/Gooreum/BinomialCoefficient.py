memo = dict()

def recursive(n, k):
    if k == 1:
        return n
    if n == k:
        return 1

    if memo.get(str(n)+":"+str(k)) == None: #이전에 저장한 값이 없다면
        keyvalue = str(n)+":"+str(k)    #키값을 만들고
        value = recursive(n-1, k-1) + recursive(n-1, k) #값을 계산해서 대입
        memo.update({keyvalue:value})   #키:값 쌍을 넣어줌

    return memo.get(str(n)+":"+str(k))

if __name__ == '__main__':
    n, k = map(int,input().split())
    print(recursive(n, k))