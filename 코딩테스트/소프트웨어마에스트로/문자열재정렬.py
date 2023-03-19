S = input()
alpha = [];nums=0
for i in S:
    if i.isalpha():
        alpha.append(i)
    else:
        nums += int(i)

alpha.sort()
print(''.join(alpha)+str(nums))