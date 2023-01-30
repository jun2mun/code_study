N, M = map(int,input().split())
S = set()
cnt = 0
for _ in range(N): # 집합 S에 포함되어 있는 문자열
    S.add(input())

for _ in range(M):
    i = input()
    if i in S:
        cnt +=1

print(cnt)