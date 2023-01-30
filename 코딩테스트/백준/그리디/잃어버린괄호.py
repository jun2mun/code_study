# - 연산자 기준으로 식을 나눈다.
expression = list(input().split('-'))
sort_expression = []

for ex in expression:
    temp = list(map(int,ex.split('+')))
    element = 0
    for x in temp:
        element += x
    sort_expression += [element]

start = sort_expression[0]
for idx in range(1,len(sort_expression)):
    start -= sort_expression[idx]

print(start)



# 55 - (50 + 60) -(30 + 50)