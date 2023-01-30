'''
문자열 슬라이싱(시간 초과)
word = input()
target = input()
start = 0
while True:
    if len(word) == 0:
        print('FRULA')
        break
    elif start + len(target) > len(word):
        print(word)
        break
    if word[start:start+len(target)] == target:
        word = word[:start] + word[start+len(target):]
        start = 0
    else:
        start+=1
'''
word = input()
target = input()
check = target[-1:]
start = 0
stack = []
for i in word:
    stack.append(i)
    if ''.join(stack[-len(target):]) == target:
        for i in range(len(target)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')

