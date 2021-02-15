#https://docs.google.com/spreadsheets/d/1vWFRyJWPBBSlo7aMolhchE9a7jn3fkO4hJI4FHLuo04/edit#gid=0
#플로이드 와샬

import sys

if __name__ == '__main__':
    node, edge = tuple(map(int, sys.stdin.readline().split()))

    for _ in range(edge):
        tuple(map(int, sys.stdin.readline().split()))