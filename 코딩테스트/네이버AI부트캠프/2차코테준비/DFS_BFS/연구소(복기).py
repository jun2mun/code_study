from collections import deque
from itertools import combinations
# 0 빈칸 1 벽 2 바이러스
def bfs(start):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    count = 1
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    while q:
        nx,ny = q.popleft()
        for x,y in zip(dx,dy):
            if 0 <= nx+x < len(graph) and 0 <= ny+y < len(graph[0]):
                if visited[nx+x][ny+y] == False and graph[nx+x][ny+y] == 0:
                    visited[nx+x][ny+y] = True
                    q.append([nx+x,ny+y])
                    count +=1
    return count

def makewall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt+1)
                graph[i][j] = 0
            

N,M  = map(int,input().split()) # (3 ≤ N, M ≤ 8)
viruses = []
graph = []
not_visited = []
max_size = 0
for x in range(N):
    temp = list(map(int,input().split()))
    for i in range(len(temp)):
        if temp[i] == 2:
            not_visited.append([x,i])
    graph.append(temp)

answer = 0
makewall(0)
print(answer)




