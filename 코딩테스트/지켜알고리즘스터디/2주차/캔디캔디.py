M, N = map(int, input().split())
wants = []
for _ in range(N):
    wants.append(int(input()))
wants.sort()
cant = sum(wants) - M
ans = 0
for i in range(N):
    tmp = min(wants[i], cant // (N-i))
    ans += tmp**2
    cant -= tmp
print(ans % 2**64)