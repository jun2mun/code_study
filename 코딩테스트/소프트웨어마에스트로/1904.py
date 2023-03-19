# dp 1  1
# dp 2  2
# dp 3  001 110 100 3
# dp 4  5
# dp 5  00001  10000 00100  00111 10011 11001 11100 11111 8


N = int(input())
dp = [0] * (N+1)
dp[1] = 1
if N >= 2:
    dp[2] = 2
for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])