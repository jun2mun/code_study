from collections import deque
def bfs(start):
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue:
        start = queue.popleft()

        if str(start) in graph:
            for i in graph[str(start)]:
                if visited[i] == False:

                    queue.append(i)
                    visited[i] = True
                    cnt +=1
    return cnt

N,M = map(int,input().split())
graph = {}
result = []
for _ in range(M):
    A,B = map(int,input().split())
    if str(B) not in graph:
        graph[str(B)] = []
    graph[str(B)] += [A]

max_num = 0
for key in graph:
    visited = [True] + [False] * N
    value = bfs(int(key))
    if max_num < value:
        max_num = value
        result = [key]
    elif max_num == value:
        result.append(key)
        
print(' '.join(result))