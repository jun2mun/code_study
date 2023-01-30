from collections import deque
def dfs(place,queue,visited):
    dx = [1,-1,0,0]; dy = [0,0,-1,1]

    while queue:
        nx,ny = queue.popleft()

        for x,y in zip(dx,dy):
            if 0<= nx +x < 5 and 0 <= ny +y < 5:
                if visited[nx+x][ny+y] == False:
                    if place[nx+x][ny+y] == 'O':
                        queue.append([nx+x,ny+y])
                        visited[nx+x][ny+y] = 1
                        distance[nx+x][]




        

def solution(places):
    answer = []

    for place in places:
        queue = deque()
        visited = [[False]*5 for _ in range(5)]
        block = [[False]*5 for _ in range(5)]
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'X':
                    block[x][y] = True; visited[x][y] = True
                if place[x][y] == 'P':
                    queue.append([x,y])
        dfs(place,queue,visited)
    return answer