graph = [list(map(int,input().split())) for _ in range(19)]
print(graph)

# 이기는 경우의 수
# 1 : start 지점 기준으로 오른쪽으로 5칸 같은거
# 2 : start 지점 기준으로 대각선으로 5칸
# 3 : start 지점 기준으로 아래로 5칸

dx = [1,-1,0,0]; dy = [0,0,-1,1]
cnt = 0
n = 19
def omok():
    for y in range(n):
        for x in range(n):
            cur = [x,y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                cnt = 1
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n: # 구간 넘는지 점검
                    continue

                while 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny]:
                    cnt += 1
                    if cnt == 5:
                        if 0 <= nx + dx[i] < n and 0<= ny + dy[i] < n and graph[nx][ny] == graph[nx+dx[i]][ny+dy[i]]:
                            break
                        if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and graph[x][y] == graph[x - dx[i]][y - dy[i]]:  # 육목 판정 2
                            break
                        return graph[x][y], x+1, y+1  # 육목이 아닌 오목이면 return

                    nx += dx[i]
                    ny += dy[i]
        return 0, -1, -1  # 승부가 나지 않을 때



color, x, y = omok()
if not color:
    print(color)
else:
    print(color)
    print(x, y)
        
