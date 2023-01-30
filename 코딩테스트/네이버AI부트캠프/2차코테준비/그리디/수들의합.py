S = int(input())
num = 1
while True:
    if S < num:
        num -= 1
        break
    if S == num:
        break
    S -= num
    num+=1

print(num)