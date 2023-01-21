def ok(x,y,N):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False
if __name__ == '__main__':
    N = int(input())
    A = input().split()

    x,y = 0,0
    for move in A:
        print(move)
        if move == 'L':
            if ok(x,y-1,N):
                x,y = x,y-1
        elif move == 'R':
            if ok(x,y+1,N):
                x,y = x,y+1
        elif move == 'U':
            if ok(x-1,y,N):
                x,y = x-1,y
        elif move == 'D':
            if ok(x+1,y,N):
                x,y = x+1,y
    
    print(x+1,y+1)
