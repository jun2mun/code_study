N,M = map(int,input().split())
h1 = set(); h2 = set()
for _ in range(N):
    h1.add(input())
for _ in range(M):
    h2.add(input())

result = sorted(list(h1 & h2))
print(len(result))

for i in result:
    print(i)