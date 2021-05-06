# https://programmers.co.kr/learn/courses/30/lessons/60058


"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
"""


def isRight(w) -> bool:
    open_cnt = 0

    for char in w:
        if char == '(':
            open_cnt += 1
        else:
            open_cnt = max(0, open_cnt - 1)

    return open_cnt == 0


def processing(w):
    # 빈 문자열이면 빈 문자열 반환
    if len(w) == 0:
        return []

    # u와 v로 분리
    r_cnt = l_cnt = 0
    u = []
    v = []

    for seq, char in enumerate(w):
        if char == '(':
            r_cnt += 1
        else:
            l_cnt += 1

        if r_cnt == l_cnt:
            u.extend(w[:seq+1])
            v.extend(w[seq+1:])
            break

    # u가 올바른 괄호인 경우
    if isRight(u):
        u.extend(processing(v))
        return u
    # u가 올바른 괄호가 아닌 경우
    else:
        result = ['(']
        result.extend(processing(v))
        result.extend([')'])

        for i in range(1, len(u) - 1):
            if u[i] == '(':
                result.append(')')
            else:
                result.append('(')

        return result


def solution(p):
    return "".join(processing(p))


if __name__ == '__main__':
    solution("")    # ""
    solution("(()())()")  # "(()())()"
    solution(")(")  # "()"
    solution("()))((()")  # "()(())()"
