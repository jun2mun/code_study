def bfs(q,start):
    visited[start] = 1
    q.append(start)
    while q:
        cur = q.popleft()
        print(cur,end=" ")
        for i in sorted(graph[cur]):
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

def dfs(cur):
    visited[cur] = 1 # 1번. 방문 처리
    print(cur,end=" ")
    for i in sorted(graph[cur]): # 인접 리스트 mutation
        if visited[i] == 0:  # 2번 방문 안했을 경우 방문
            dfs(i)


from collections import deque
N, M, V = map(int,input().split())
graph = dict(); visited = [1] + [0] * (N)
for _ in range(M):
    A, B = map(int,input().split())
    if A in graph:
        graph[A] += [B]
    else:
        graph[A] = [B]

    if B in graph:
        graph[B] += [A]
    else:
        graph[B] = [A]

queue = deque()
dfs(V)
visited = [1] + [0] * (N)
print()
bfs(queue,V)