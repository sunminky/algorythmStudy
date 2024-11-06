# https://www.acmicpc.net/problem/2156

def solution(arr):
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    operators = [arr[i] for i in range(1, len(arr), 2)]
    calc = [[[-100001, 100001] for _ in range(len(nums))] for _ in range(len(nums))]  # 최대 최소

    for i in range(len(nums)):
        calc[i][i] = [nums[i], nums[i]]

    for i in range(1, len(nums)):
        for row in range(len(nums) - i):
            for col in range(row, row + i):
                if operators[col] == '+':
                    calc[row][row + i][0] = max(calc[row][row + i][0], calc[row][col][0] + calc[col + 1][row + i][0])
                    calc[row][row + i][1] = min(calc[row][row + i][1], calc[row][col][1] + calc[col + 1][row + i][1])
                else:
                    calc[row][row + i][0] = max(calc[row][row + i][0], calc[row][col][0] - calc[col + 1][row + i][1])
                    calc[row][row + i][1] = min(calc[row][row + i][1], calc[row][col][1] - calc[col + 1][row + i][0])

    return calc[0][-1][0]


if __name__ == '__main__':
    solution(["1", "-", "3", "+", "5", "-", "8"])  # 1
    solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])  # 3
    solution(["10", "-", "0", "-", "10", "-", "10", "+", "10", "-", "10"])  # 50
