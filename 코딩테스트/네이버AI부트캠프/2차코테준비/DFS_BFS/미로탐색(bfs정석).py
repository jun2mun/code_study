from collections import deque

def bfs(start,end,visited):
    queue = deque([start])
    count = [[0] * M for _ in range(N)]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue:
        nx,ny = queue.popleft()
        if [nx,ny] == end:
            return count[nx][ny] + 1
        for x,y in zip(dx,dy):
            if 0 <= nx+x < len(visited) and 0<= ny + y < len(visited[0]):
                if visited[nx+x][ny+y] == 0 and graph[nx+x][ny+y] != 0:
                    visited[nx+x][ny+y] = 1
                    count[nx+x][ny+y] = count[nx][ny] + 1
                    queue.append([nx+x,ny+y])



N, M = map(int,input().split()) #(2 ≤ N, M ≤ 100)
graph = []

for _ in range(N):
    graph.append(list(map(int,input())))
visited = [[False] * M for _ in range(N)]

answer = bfs([0,0],[N-1,M-1],visited)
print(answer)



