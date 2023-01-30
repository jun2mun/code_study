
N , K = map(int,input().split()) # (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
coins = []; total = 0
for _ in range(N):
    coins.append(int(input()))
for i in range(len(coins)-1,-1,-1):
    cnt = 0
    if K == 0:
        break
    if K//coins[i] > 0:
        cnt = K//coins[i]
        K -= coins[i]*cnt
        total += cnt
        

print(total)