N = list(map(int,input())) # 점수
n  = len(N)
left = 0 ; right = 0
for idx in range(n):

    if idx < n //2:
        left += N[idx]
    else:
        right += N[idx]

print('LUCKY' if left == right else 'READY')