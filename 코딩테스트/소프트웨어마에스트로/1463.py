# 3 나누기
# 2 나누기
# 1 빼기

num = int(input())
d = [0] * (num+1)

for i in range(2, num+1):

    d[i] = d[i-1] + 1 # 1 더하는 방법 (1회)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1) # 3을 곱하여 1회 더할때랑 횟수 비교
    if i %2 == 0:
        d[i] = min(d[i],d[i//2] + 1)

print(d[num])





