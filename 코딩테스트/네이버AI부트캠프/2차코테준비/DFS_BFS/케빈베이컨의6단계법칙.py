from collections import deque
def bfs(cur):
    visited = [False]*(N+1)
    count = [0] * (N+1)
    queue = deque()
    queue.append(cur)
    visited[cur] = True
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                count[i] += (count[cur] + 1)
    total = 0
    for i in count:
        total += i
    return total

N,M = map(int,input().split())
graph = {}
count_list = [0] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    if not a in graph:
        graph[a] = []
    if not b in graph:
        graph[b] = []
    graph[a] += [b]
    graph[b] += [a]
min_num = 100000
answer = []
for user in range(1,N+1):
    total = bfs(user)
    answer.append([user,total])

print(sorted(answer,key=lambda x:x[1])[0][0])

