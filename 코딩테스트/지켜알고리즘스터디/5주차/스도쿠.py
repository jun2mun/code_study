def checkRow(x,n):
    for i in range(9): # 스도쿠 9개
        if n == graph[x][i]: # 행 검사
            return False
    return True

def checkCol(y,n):
    for i in range(9): # 스도쿠 9개
        if n == graph[i][y]: # 열 검사
            return False
    return True

def checkRect(x,y,n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    # 대각선 검사
    for i in range(3):
        for j in range(3):
            if n == graph[nx+i][ny+j]:
                return False
    return True

def dfs(n):
    # 스도쿠의 빈 칸을 채웠다면
    if n == len(blank):
        for _ in range(9):
            print(*graph[_]) ## 해당 코드는 인터넷 참조
        exit(0)

    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1] 

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(n + 1)
            graph[x][y] = 0

import sys
graph = []
blank = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i, j])
dfs(0)