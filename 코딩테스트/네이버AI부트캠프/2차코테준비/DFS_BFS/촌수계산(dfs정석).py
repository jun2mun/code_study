def dfs(cur,cnt):
    global answer
    visited[cur] = True
    if cur == target:
        answer = cnt
        return
    for i in graph[cur]:
        if visited[i] == False:
            dfs(i,cnt+1)
    
graph = dict()
n = int(input())
start,target = map(int,input().split())
m = int(input())
visited = [True] + [False] * (n)
for _ in range(m):
    x,y = map(int,input().split())
    if not x in graph:
        graph[x] = []
    if not y in graph:
        graph[y] = []
    graph[x] += [y]
    graph[y] += [x]
answer = -1
dfs(start,0)
print(answer)