N = list(input())
N.sort(reverse=True)
answer = ''
if N[-1] != '0': # 최소 0이 한개 있어야 함
    print(-1)
else:
    for num in N:
        answer += num
    if int(answer) % 3 != 0:
        print(-1)
    else:
        print(int(answer))