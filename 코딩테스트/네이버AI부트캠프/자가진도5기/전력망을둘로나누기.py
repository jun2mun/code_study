def DFS(v,graph,visited,chk_list):
    cnt = 1
    visited[v] = True

    for adj_v in graph[v]:
        if visited[adj_v] == False and chk_list[v][adj_v]:
            cnt += DFS(adj_v,graph,visited,chk_list)
    
    return cnt

def solution(n, wires):
    answer = 10000000

    chk_list = [[True] * (n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for wire in wires:
        # Graph 생성 
        x,y = wire
        graph[x].append(y)
        graph[y].append(x)


    for x,y in wires:
        visited = [False] * (n+1)
        chk_list[x][y] = False
        cnt_a = DFS(x,graph,visited,chk_list)
        cnt_b = DFS(y,graph,visited,chk_list)
        chk_list[x][y] = True

        answer = min(answer,abs(cnt_a - cnt_b))        

    return answer

if __name__ == '__main__':
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n,wires))