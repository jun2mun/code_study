import sys
input = sys.stdin.readline


def DFS(iter,idx):
    global result


    if iter == (N // 2): # 짝수로 주이지기 때문에 짝수만큼 진행
        linkteam = 0 ; starteam = 0
        for i in range(N):
            for j in range(i+1,N):# i+1 0 0 제외
                if visited[i] and visited[j]:
                    linkteam += (graph[i][j] + graph[j][i])

                elif not visited[i] and not visited[j]:
                    starteam += (graph[i][j] + graph[j][i])
            
        result = min(result,abs(linkteam-starteam))
        return

            
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True # 방문
            DFS(iter+1,i+1) # 방문 처리 후 (나머지 애들 백트래킹) || 재귀
            visited[i] = False # 방문처리 빼기


result = sys.maxsize
N = int(input()) # 축구를 하기 위해 모인 사람 (4<=N<=20) N은 짝수
visited = [0 for _ in range(N)] # 방문여부 (사람별로) # 1차원
graph = [list(map(int,input().split())) for _ in range(N)] # 능력치 행렬
DFS(0,0)
print(result)