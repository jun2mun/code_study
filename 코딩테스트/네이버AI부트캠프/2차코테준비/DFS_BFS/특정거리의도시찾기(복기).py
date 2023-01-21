def dfs(cur,cost,stop):
    if len(roads[cur]) == 0 or cur == stop or not(False in visited):
        if cost == K:
            city.append(stop)
        return

    for target in roads[cur]:
        if visited[target-1] == 0: # no 방문시
            visited[target-1]  = 1
            dfs(target,cost+1,stop)
            visited[target-1] = 0

if __name__ == '__main__':
    N,M,K,X = map(int,input().split()) # 도시의 개수 , 도로의 개수, 거리 정보, 출발 도시의 번호
    roads = [[] for _ in range(M)]
    for _ in range(M):
        road = list(map(int,input().split()))
        roads[road[0]] += [road[1]]

    #print(roads)
    visited = [0]* N; visited[X] = 1
    city = []
    for i in range(N):
        dfs(X-1,0,N)
    city.sort()
    if len(city) == 0:
        print(-1)
    else:
        print(city)
    
        
