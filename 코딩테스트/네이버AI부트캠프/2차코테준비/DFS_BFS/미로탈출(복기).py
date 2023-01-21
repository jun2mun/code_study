def dfs(idx,idy,cnt):
    global answer
    dx = [1,-1,0,0]; dy = [0,0,-1,1]
    if idx == N-1 and idy == M-1:
        answer = min(answer,cnt)

    for x,y in zip(dx,dy):
        if 0 <= idx+x < N and 0 <= idy+y < M:
            if graph[idx+x][idy+y] == 1 and visited[idx+x][idy+y] == False:
                visited[idx+x][idy+y] = True
                dfs(idx+x,idy+y,cnt+1)
                visited[idx+x][idy+y] = False




if __name__ == '__main__':
    N,M = map(int,input().split())
    answer = 100000
    # 동빈 (1,1) 출구 (N,M) 한칸씩 이동
    graph = []; visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int,input())))
    dfs(0,0,0)

    print(answer)