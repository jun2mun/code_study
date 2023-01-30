N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
total = 0
answer = []
for idx,num in enumerate(B):
    answer += [[idx,num]]

answer.sort(key=lambda x :x[1],reverse=True)
A.sort()

for a,b in zip(A,answer):
    total += a* b[1]
print(total)