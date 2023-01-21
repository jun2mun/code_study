def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
        
        return True

def n_queens(n,x):
    global ans
    if x == n:
        ans +=1
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(n,x+1)


if __name__ == '__main__':
    N = int(input()) # 1<= N < 15
    
    ans = 0
    row = [0] * N

    n_queens(N,0)
