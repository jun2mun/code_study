def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction = 3

if __name__ == '__main__':

    N, M = map(int,input().split())
    nx,ny,direction = map(int,input().split())
    
    d = [[0] * M for _ in range(N)]
    graph = []

    for i in range(N):
        graph.append(list(map(int,input().split())))

    dx = [-1,0,1,0]; dy= [0,1,0,-1]

    count = 1
    turn_time = 0
    while True:
        turn_left()
        x = nx + dx[direction]
        y = ny + dy[direction]

    #,,,



