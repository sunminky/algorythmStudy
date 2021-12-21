# https://programmers.co.kr/learn/courses/30/lessons/86053
def solution(a, b, gold, silver, capacity, timecost):
    start = 0
    end = 400000000000000

    table = [{'gold': gold[i], 'silver': silver[i], 'capacity': capacity[i], 'timecost': timecost[i]} for i in range(len(gold))]

    while start < end:
        middle = (start + end) // 2
        mine_gold = a
        mine_silver = b
        mine_all = a + b

        for e in table:
            times = (middle // e['timecost'] + 1) // 2
            mine_gold -= min(times * e['capacity'], e['gold'])
            mine_silver -= min(times * e['capacity'], e['silver'])
            mine_all -= min(times * e['capacity'], e['gold'] + e['silver'])

        if mine_gold <= 0 and mine_silver <= 0 and mine_all <= 0:
            end = middle
        else:
            start = middle + 1

    return end


if __name__ == '__main__':
    solution(10, 10, [100], [100], [7], [10])  # 50
    solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1])  # 499
    solution(100, 1000, [100, 100], [0, 1000], [10, 1000], [10, 100])  # 190
