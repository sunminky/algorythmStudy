import random

#밀러라빈 소수판별 법
def isprime(n):
    if n == 2:
        return True
    if n < 2 or not n & 1:
        return False
    def mrtest(b):
        x = pow(b, t, n)
        if x == 1:
            return True
        for i in range(s):
            if x == n - 1:  #나머지가 -1
                return True
            x = pow(x, 2, n)
        return False
    #n이 소수일 때, n -1 = t * pow(2, s), t는 홀수
    s = 0
    t = n - 1
    #t가 홀수가 될 때까지 2로 나눔
    while not t & 1:
        s += 1
        t >>= 1
    #n보다 작은 양의 정수에 대해 밀러라빈 판별식 10번 수행
    for i in range(10):
        b = random.randrange(2, n)
        #밀러라핀 판별식 1번 수행할 때마다 틀릴 확률이 75% 감소
        if not mrtest(b):
            return False
    return True

if __name__ == '__main__':
    for e in [7919, 7907, 7901, 7883, 7879, 7877, 7873, 7867, 7853, 7841, 7829, 7823, 7817, 7793, 7789, 7759, 7757]:
        print(isprime(e))