
# 500 100 50 10
# 동전 최소 개수
N = 1260 ; cnt = 0

coins = [500,100,50,10]

for coin in coins:
    cnt += N // coin
    N = N % coin

print(cnt)
