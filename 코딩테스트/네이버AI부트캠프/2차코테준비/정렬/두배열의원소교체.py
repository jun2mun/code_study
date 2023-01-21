
if __name__ == '__main__':
    N,K = map(int,input().split())
    A = []; B =[]; answer =0
    for i in range(2):
        if i == 0:
            A = list(map(int,input().split()))
        else:
            B = list(map(int,input().split()))
    
    A.sort(); B.sort(reverse=True)
    for i in range(K):
        if A[i] < B[i]:
            A[i],B[i] = B[i],A[i]
        else:
            break
    for a in A:
        answer += a
    
    print(answer)
