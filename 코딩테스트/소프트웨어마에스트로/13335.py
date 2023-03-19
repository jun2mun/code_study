from collections import deque
n,w,L = map(int,input().split())
trucks = list(map(int,input().split()))
bridge = deque([0]*w)
time = 0
idx = 0
while True:
    time +=1 # 시간이 흐름
    out = bridge.popleft() # 다리에서 나가는 트럭
    if sum(bridge) + trucks[idx] > L: # 최대 하중을 넘기면 트럭 진입 불가
        bridge.append(0) # dummy 데이터 입력
    else:
        bridge.append(trucks[idx])
        idx +=1

    if idx == len(trucks):
        break

print(time+w)

    