N = int(input()) #(1 ≤ N ≤ 100,000)

consults = []
for _ in range(N):
    consults.append(list(map(int,input().split())))

consults.sort(key=lambda x: x[0])
consults.sort(key=lambda x: x[1])

print(consults)