if __name__ == '__main__':
    N = list(map(int,input()))
    mid = len(N) /2
    left = 0; right = 0
    for idx in range(len(N)):
        if idx < mid:
            left += N[idx]
        else:
            right += N[idx]
    
    if left == right:
        print('LUCKY')
    elif left != right:
        print('READY')
        