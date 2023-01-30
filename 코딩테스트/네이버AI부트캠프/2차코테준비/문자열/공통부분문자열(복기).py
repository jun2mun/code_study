A = input()
B = input()

dp = [[0] * len(A) for _ in range(len(A))]

for start in range(len(A),-1,-1):
    for idx in range(len(A)):    
        A[idx:start]
