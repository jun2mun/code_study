def dfs(x,y,visited,route,prob):
    global 단순한_경우의_수
    E_p,W_p,N_p,S_p = prob
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[x][y] = True
    if len(route) == N:
        단순한_경우의_수 +=1
        return


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(visited) and 0<=ny < len(visited[0]):
            if visited[nx][ny] == True:
                continue
            else:
                if prob[i] == 0:
                    continue
                visited[nx][ny] = True
                dfs(nx,ny,visited,route+'o',prob)
                visited[nx][ny] = False
        
    return



if __name__ == "__main__":
    N, E_p,W_p,N_p,S_p = map(int,input().split())
    probs = [E_p,W_p,N_p,S_p]; avl = 0
    단순한_경우의_수 = 0
    for prob in probs:
        if prob != 0:
            avl +=1

    전체_경우의_수 = avl ** N

    visited = [[False for _ in range(2*N+1)] for _ in range(2*N+1)] # 전체 맵
    
    dfs(N,N,visited,'',probs)

    answer = round(단순한_경우의_수 / 전체_경우의_수,20)
    print(answer)
