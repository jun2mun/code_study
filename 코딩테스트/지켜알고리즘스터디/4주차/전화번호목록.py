import sys
t = int(sys.stdin.readline())
for _ in range(t):
    num = int(sys.stdin.readline())
    temp = [];  find = False
    for _ in range(num):
        temp.append(sys.stdin.readline().rstrip())
    temp.sort()
    for i in range(len(temp)-1):
        if temp[i] ==  temp[i+1][0:len(temp[i])]:
            find = True
            break
    
    if find == True:
        print('NO')
    else:
        print('YES')
    