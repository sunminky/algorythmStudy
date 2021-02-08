import sys


def solution(begin, target, words):
    neighbor = [[cmpWord(words[i], words[j]) for j in range(len(words))] for i in range(len(words))]
    begin = [cmpWord(begin, words[i]) for i in range(len(words))]
    depth = list(map(lambda x: 1 if x else sys.maxsize, begin))
    isLeft = True
    cnt = 1
    answer = 0

    while isLeft:
        isLeft = False
        for seq, dep in enumerate(depth):
            if dep == cnt:
                for j in range(len(neighbor[seq])):
                    if neighbor[seq][j]:
                        if depth[j] > depth[seq]+1:
                            depth[j] = depth[seq]+1
                isLeft = True
        cnt += 1

    for i in range(len(neighbor)): # target과 같은 문자열의 깊이 찾기
        if target == words[i]:
            answer = depth[i]
            break

    if answer == sys.maxsize:
        answer = 0

    return answer


def cmpWord(src, dst):  # 단어가 한글자 빼고 같은지 체크
    diffCnt = 0
    if src == dst:
        return None

    for seq in range(len(src)):
        if src[seq] != dst[seq]:
            diffCnt += 1
        if diffCnt > 1:
            return False
    return True


if __name__ == '__main__':
    ret = solution("hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log', 'cog', 'sot', 'cok', 'pot'])
    print(ret)