# https://www.acmicpc.net/problem/1111
import sys


def find(n_num, nums) -> str:
    if n_num == 1:
        return 'A'
    if len(set(nums)) == 1:
        return nums[0]
    if n_num == 2:
        return 'A'
    # nums[1] - nums[0] 이 0이 되면 안됨
    if nums[1] == nums[0]:
        return 'B'

    a = (nums[2] - nums[1]) // (nums[1] - nums[0])
    b = nums[1] - a * nums[0]

    for i in range(1, n_num):
        if nums[i - 1] * a + b != nums[i]:
            return 'B'

    return nums[-1] * a + b


if __name__ == '__main__':
    n_num = int(sys.stdin.readline())
    nums = tuple(map(int, sys.stdin.readline().split()))

    print(find(n_num, nums))
