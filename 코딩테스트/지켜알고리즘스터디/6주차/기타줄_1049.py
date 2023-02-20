def calc(N):
    # 시간 초과가 나기 때문에 , 
    # 6개 이하로 남은 기타줄을  낱개로 살 때와 패키지로 살때 무엇이 더 비용이 덜 드는지 비교해야함.
    pay = 0
    if 6 * line[0][1] >= packages[0][0]: # 낱개 6개 가격 >= 패키지 가격
        pay = (N//6) * packages[0][0] + (N % 6) * line[0][1]
        if packages[0][0] < line[0][1] * (N%6): # 남은 낱개 n개 가격 >= 패키지 가격
            pay = packages[0][0] * (N//6 +1)
    else:
        pay = N * line[0][1]
        
    return pay

if __name__ == '__main__':
    N,M = map(int,input().split())
    guitars = []
    for _ in range(M):
        guitars += [list(map(int,input().split()))]
    
    packages = sorted(guitars,key=lambda x:x[0])
    line = sorted(guitars,key=lambda x:x[1])
    
    pay = calc(N)
    
    print(pay)

    # N 이 6개 이상인 경우 : 패키지 사야함(최소 가격 패키지)
    # N 이 6개 미만인 경우 : 낱개중에서 (최소 가격 낱개)
