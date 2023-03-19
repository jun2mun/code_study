def convert(_list,M,N):
    if _list[0] == 1:
        return 0,_list[1]
    elif _list[0] == 2:
        return M,_list[1]
    elif _list[0] == 3:
        return _list[1],0
    elif _list[0] == 4:
        return _list[1],N


M,N = map(int,input().split())
cnt = int(input())
stores = []
for _ in range(cnt):
    stores += [list(map(int,input().split()))]

result = 0
dongeun = list(map(int,input().split()))

x,y = convert(dongeun,M,N)
for store in stores:
    store_x,store_y = convert(store,M,N)
    print(result)
    if store_x == x: # 같은 줄에 있을 경우
        diff = abs(store_y-y)
        result += diff
    if store_y == y: # 같은 줄에 있을 경우
        diff = abs(store_x-x)
        result += diff

    if store_x == 0 and y == 0: #북서
        diff = store_y + x
        result += diff

    if store_x == 0 and y == N: # 북동
        diff = (N-store_y) + x
        result += diff

    if store_y == y : # 북남
        diff = min(N-y,y) *2 + M
        result += diff

print(result)

# 북 : (0,a)
# 서 : (a,0)
# 동 : (a,N)
# 남 : (M,a)
    
    


# 북/남 왼쪽으로부터 거리 (1 or 2 , 4) => (0 or m,4)
# 동/서 위쪽으로부터 거리 (3 or 4 , 2) => (2 , n or 0)

# 거리 계산 (0,4) 와 (5,3) / (0,4) 와 (5,)

# 같은 줄에 있을 경우

# 반대편에 있을 경우
# 직각 줄에 있을 경우