def dfs(nx,ny,visit):
        
    dx = [1,-1,0,0]; dy=[0,0,-1,1]
    visited[nx][ny] = True
    
    for x,y in zip(dx,dy):
        if 0<= nx+x < N and 0<= ny+y < M:
            if visited[nx][ny] == False:
                dfs(nx+x,ny+y,visit+1)

    


    pass

if __name__ == '__main__':
    N,M = map(int,input().split())
    graph = []; visited = [[False for _ in range(M)] for _ in range(N)]
    not_visted = []
    for i in range(N):
        temp_list = list(map(int,input()))
        for k in range(len(temp_list)):
            if k == 0:
                not_visted.append([i,k])
    

