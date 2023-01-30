def check(x,y):
    for m in range(3):
        for n in range(3):
            if A[x+m][y+n] != B[x+m][y+n]:
                return True
    return False

def reverse(x,y):
    for m in range(3):
        for n in range(3):
            if A[x+m][y+n] == 0:
                A[x+m][y+n] = 1
            elif A[x+m][y+n] == 1:
                A[x+m][y+n] = 0

N, M = map(int,input().split()) # N과 M은 50보다 작거나 같은 자연수
A = []; B = []

for _ in range(N):
    A += [list(map(int,input()))]
for _ in range(N):
    B += [list(map(int,input()))]

if N < 3 or M <3:
    if A == B:
        print(0)
        exit()
    else:
        print(-1)
        exit()

cnt = 0
for x in range(N-2):
    for y in range(M-2):
        if check(x,y):
            cnt +=1
            reverse(x,y)

if A != B:
    print(-1)
else:
    print(cnt)

#홀짝짝홀

