
def solution():
    N = int(input()) # 돌상의 개수
    left = 0; right =0
    rocks = list(map(int,input().split())) # 돌상의 리스트

    while True:
        if len(rocks) == 0:
            break
        out = rocks.pop(0)
        if out == '1':
            left +=1
        if out == '2':
            right +=1
    
    answer = abs(left-right)
    print(answer)

import math
def solution2():
    N = int(input()) # 돌상의 개수
    left = 0; right =0; total = 0
    rocks = list(map(int,input().split())) # 돌상의 리스트
    answer = [[-math.inf for _ in range(N)] for _ in range(N)]
    max_count = -math.inf
    for x in range(N):
        if rocks[x] == 1:
            answer[x][x] = 1
        else:
            answer[x][x] = -1
    #print(answer)
    
    if N == 1:
        print(1)
        exit()

    for y in range(N-1,-1,-1):
        for x in range(y-1,-1,-1):
            #print(answer[x][y],answer[x][x],answer[x+1][y])
            answer[x][y] = answer[x][x] + answer[x+1][y]
            max_count = max(abs(answer[x][y]),1)

    
    print(max_count)


