from collections import deque
def DFS(idx,idy,sheep,wolf):
    global sheeps; global wolfs
    visited[idx][idy] = True
    for x,y in zip(dx,dy):
        if 0<= x+idx < R and 0<= y+idy < C and visited[x+idx][y+idy] == False and graph[idx+x][idy+y] != '#':
            if graph[idx+x][idy+y] == 'v':
                DFS(idx+x,idy+y,sheep,wolf+1)
            elif graph[idx+x][idy+y] == 'k':
                DFS(idx+x,idy+y,sheep+1,wolf)
            elif graph[idx+x][idy+y] == '.':
                DFS(idx+x,idy+y,sheep,wolf)

if __name__ == '__main__':
    R, C = map(int,input().split())
    #graph = [list(input().split()) for _ in range(C)]
    graph =[['...#..'], ['.##v#.'], ['#v.#.#'], ['#.k#.#'], ['.###.#'], ['...###']]
    queue = deque([[1,3],[2,1],[3,2]])
    visited = [[False] * C for _ in range(R)]
    dx = [1,0,0,-1]; dy = [0,1,-1,0]
    answer_sheep=0; answer_wolf = 0
    while queue:
        sheeps = 0; wolfs = 0
        nx,ny = queue.popleft()
        DFS(nx,ny,0,0)
        if sheeps > wolfs:
            answer_sheep += sheeps
        else:
            answer_wolf += wolfs

