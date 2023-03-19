# 1 1
# 2 1
# 3 1
# 4 1

# 4 1
# 4 2
# 4 3
# 4 4

# 왼쪽 -> 아래
# (x,1) -> (M,)

N,M,R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N,M)// 2):
        x,y = i,i
        value = graph[x][y]

def left():
    for i in range(0,M):
