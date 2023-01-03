def solution(n, money):
    answer = 0
    
    dp = [1] + [0] * (n)
    for num in money:
        for i in range(num,n+1):
            dp[i] = (dp[i] + dp[i-num]) % 1000000007

    answer = dp[n]


if __name__ == '__main__':
    pass