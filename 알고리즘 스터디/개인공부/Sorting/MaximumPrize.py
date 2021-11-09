# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&

if __name__ == '__main__':
    for tc in range(int(input())):
        target, remain = input().split()
        ideal = sorted(target, reverse=True)
        target = list(target)
        remain = int(remain)

        for i in range(len(target)):
            if target[i] == ideal[i]:
                continue

            candidate = tuple(filter(lambda x: target[x] != ideal[x] and ideal[i] == target[x], range(i + 1, len(target))))

            for e in candidate:
                if ideal[e] == target[i]:
                    target[i], target[e] = target[e], target[i]
                    break
            else:
                target[i], target[candidate[0]] = target[candidate[0]], target[i]

            remain -= 1

            if remain == 0:
                break

        if remain % 2 == 0 or remain == 0:
            pass
        # 같은 수 존재
        else:
            cnt = [0] * 10

            for e in target:
                cnt[int(e)] += 1

                if cnt[int(e)] > 1:
                    break
            else:
                # 제일 작은거 두개 바꿈
                target[-1], target[-2] = target[-2], target[-1]

        print(f"#{tc + 1} {''.join(target)}")
