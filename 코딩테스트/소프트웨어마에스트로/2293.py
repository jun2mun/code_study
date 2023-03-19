n,k = map(int,input().split())

# dp 1 1
# dp 2 2
# dp 3 3
# dp 4 5
# dp 5 9  11111  1112 1121 1211 2111  122 212 221 5
# dp 6 15  111111 11112 11121 11211 12111 21111 1122 1221 1212 2112
# 2121 2211 222 15 51  
n, k = map(int, input().split())
c = []
dp = [0 for i in range(k + 1)]
dp[0] = 1
for i in range(n):
    c.append(int(input()))
for i in c:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])