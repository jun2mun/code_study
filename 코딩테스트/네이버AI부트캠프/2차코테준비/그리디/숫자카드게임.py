if __name__ == '__main__':
    answer = -1
    N,M = map(int,input().split())
    for _ in range(N):
        min_num = sorted(list(map(int,input().split())))
        min_num = min_num[0]
        answer = max(answer,min_num)
    
    print(answer)