N = int(input())
cows = [list(map(int,input().split())) for _ in range(N)]
cows.sort(key=lambda x :x[0])
start = cows[0][0]
total = 0
for idx in range(len(cows)-1):
    if start + cows[idx][1] > cows[idx+1][0]:
        # iteration의 start 포인트에서 그 iter의 검문시간 더했을시 
        # 소의 도착 시각 보다 늦을 경우 소의 출발 시간을 늦춘다.
        start += cows[idx][1]
    else:
        # 소의 도착 시각보다 빠른 경우 소의 도착시간에 start 한다.
        start = cows[idx+1][0]

print(start + cows[-1][1]) # start 포인트에서 마지막 검문시간 더하기
        
