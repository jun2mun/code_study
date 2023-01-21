if __name__ == '__main__':
    N,M,K = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort(reverse=True)
    max_num = 0

    for idx in range(1,M+1):
        if idx % K == 0:
            max_num += data[1]
        else:
            max_num += data[0]
    
    print(max_num)
        
