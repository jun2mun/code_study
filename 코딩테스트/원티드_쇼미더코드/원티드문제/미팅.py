
def dfs(idx,idy,a,b,cost): # a가 b보다 긴 경우
    global answer

    i = 0
    while True:
        print(a,b,cost,"iter start")

        if len(b) == 0:
            answer = max(answer,cost) # 더 큰 값에 answer 할당
            return
        #a = a[i+1:]; b = b.pop(0)
        if i+1 > len(a):
            return
        print(A[idx]-1,B[idy]-1, graph[A[idx]-1][B[idy]-1])
        print("=========",a,b)
        dfs(idx+i+1,idy+1,a[i+1:],b[1:],cost+ graph[A[i+idx]-1][B[idy]-1])
        print("iter end")

        i +=1


if __name__ == '__main__':
    answer = 0
    graph = []; A=[]; B=[]
    N,M,C = map(int,input().split()) # A 대학 N명, B대학 M명 , C 성격 #232
    
    # 성격 그래프
    #for _ in range(C):
    #    graph.append(list(map(int,input().split())))

    graph = [[1, 10], [10, 10]] # 0,0 0,1 1,0 1,1

    # 11 22 00 11 1 + 10 = 11
    # 12 01 10 

    # 학생 성격 정보 
    '''
    for idx in range(1,3):
        if idx ==1:
            A = list(map(int,input().split()))
        if idx ==2:
            B = list(map(int,input().split()))
    '''
    A,B = [1, 2],[1, 2, 2]

    if N> M : # A 대학 사람이 더 많음
        for i in range(N-M):
            dfs(0,0,A,B,0)# i 번째 학생부터 악수 시작 
    else : 
        for i in range(M-N):
            A,B = B,A
            dfs(0,0,A,B,0)# i 번째 학생부터 악수 시작 
    
    print(answer)
