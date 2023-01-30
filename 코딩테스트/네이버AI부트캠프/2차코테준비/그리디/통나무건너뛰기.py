# 레벨 : 통나무의 높이 차
T = int(input())
for _ in range(T):
    N = int(input())
    L = sorted(list(map(int,input().split())))
    answer = [0] * N

    start = 0; end = N-1
    left = True; idx = 0
    while True:
        if start > end:
            break
        if left == True:
            answer[start] = L[idx]
            start +=1
            left = False
        else:
            answer[end] = L[idx]
            end -=1
            left = True
        idx +=1
    diff = -1
    for i in range(N):
        diff = max(diff,abs(answer[i-1]-answer[i]))
    print(diff)