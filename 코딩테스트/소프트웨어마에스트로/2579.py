
stairs_num = int(input())
stairs_scores = []
dp = [0] * (stairs_num + 1)
for _ in range(stairs_num):
    stairs_scores += [int(input())]
if len(stairs_scores)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(stairs_scores))
else:
    dp[0] = stairs_scores[0]
    dp[1] = stairs_scores[0] + stairs_scores[1]
    dp[2] = max(stairs_scores[1] + stairs_scores[2], stairs_scores[0] + stairs_scores[2])

    for i in range(3,stairs_num):
        dp[i] = max(dp[i-3] + stairs_scores[i] + stairs_scores[i-1] , dp[i-2] + stairs_scores[i])