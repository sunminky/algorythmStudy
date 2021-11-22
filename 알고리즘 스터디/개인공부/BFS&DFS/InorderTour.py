# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV140YnqAIECFAYD&categoryId=AV140YnqAIECFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=3&&&&&&&&&&
def touring(cur_node, node):
    if cur_node * 2 <= len(node):
        touring(cur_node * 2, node)  # 왼쪽

    print(node[cur_node - 1][0], end="")  # 가운데

    if cur_node * 2 + 1 <= len(node):
        touring(cur_node * 2 + 1, node)  # 오른쪽


if __name__ == '__main__':
    for tc in range(1, 11):
        length = int(input())
        node = [None] * length

        for _ in range(length):
            seq, alphabet, *child = input().rstrip().split()
            node[int(seq) - 1] = [alphabet, child]

        print(f"#{tc} ", end="")
        touring(1, node)
        print()
