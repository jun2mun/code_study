import sys
from collections import deque


# 21% 실패
def _water():
    global water
    water_plus = []

    while water:
        x, y = water.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == ".":
                    graph[nx][ny] = "*"
                    visited[nx][ny] = -1
                    water_plus.append([nx, ny])

    for a, b in water_plus:
        water.append([a, b])


def bfs():
    global queue

    while queue:
        queue_plus = []
        while queue:

            x, y = queue.popleft()
            
            #############여기###############

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == "D":
                        return visited[x][y] + 1

                    elif graph[nx][ny] == "." and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue_plus.append([nx, ny])

        for a, b in queue_plus:
            queue.append([a, b])

        _water()

    return "KAKTUS"


r, c = map(int, sys.stdin.readline().split())

graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

queue = deque([])
water = deque([])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == "S":
            queue.append([i, j])

        elif graph[i][j] == "*":
            water.append([i, j])

print(bfs())