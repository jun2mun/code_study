from collections import deque

N,K = map(int,input().split())
array = [0] * 100001
def bfs(N,K):
    cur = N;     time = 0
    queue = deque()
    queue.append(cur)

    while queue:
        cur= queue.popleft()
        if cur == K:
            return array[K]
        for i in (cur-1,cur+1,cur*2):
            if 0<= i <= 100000:
                if array[i] == 0:
                    array[i] = array[cur] +1
                    queue.append(i)

print(bfs(N,K))