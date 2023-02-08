from collections import deque
def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y))
    count = 1
    visited[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    while queue:
        nx,ny = queue.popleft()
        for x,y in zip(dx,dy):
            if 0<= nx+x < len(graph) and 0<= ny+y < len(graph):
                if visited[nx+x][ny+y] == False and graph[nx+x][ny+y] ==1:
                    visited[nx+x][ny+y] = True
                    count +=1
                    queue.append([nx+x,ny+y])
    
    return count
                    



N = int(input()) 
graph = []; town_list = deque()
visited = [[False]* N for _ in range(N)]
for i in range(N):
    towns = list(map(int,input()))
    for idx in range(len(towns)):
        if towns[idx] == 1: # 마을 정보 입력
            town_list.append([i,idx]) # 마을 정보 저장
    graph.append(towns)
cnt = 0; answer = []

for town in town_list: # 마을 들 뽑아서 루프
    x,y = town
    if visited[x][y] == False: # 방문 안했으면 bfs 함수 실행
        answer += [bfs(x,y,graph)]
        cnt +=1

print(cnt)
for i in sorted(answer):
    print(i)