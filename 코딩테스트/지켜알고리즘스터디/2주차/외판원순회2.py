def solution(start,me,graph,not_visited,cost):
    global answer
    # 갈 수 없는 경우 : 0
    if len(not_visited) == 0:
        if graph[me][start] != 0:
            answer = min(answer,cost+graph[me][start])
        return
    for idx in range(len(not_visited)): # 방문하지 않은 곳이 없을 때 까지
        town = not_visited[idx]
        update_visited = not_visited[:idx] + not_visited[idx+1:]
        if graph[me][town] != 0: # 방문가능한 루트 이면
            solution(start,town,graph,update_visited,cost + graph[me][town])
    
    

import math
if __name__ == '__main__':
    answer = math.inf
    N = int(input()) # 도시의 수
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    not_visited = [x for x in range(N)] # 방문하지 않은 도시 표시

    # 전부 방문해야하니까 DFS or BFS
    for i in range(N):
        solution(i,i,graph,not_visited[:i]+not_visited[i+1:],0) # cost 초기 0
        
    print(answer)
