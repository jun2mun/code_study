A = input()
B = input()
temp = B[:]
while True:
    if len(temp) == len(A):
        if temp == A:
            print(1)
            break
        else:
            print(0)
            break

    if temp[-1] == 'A': # 문자열의 뒤에 A를 추가한경우
        temp = temp[:-1]
    elif temp[-1] == 'B': # 문자열을 뒤집고 뒤에 B를 추가한 경우
        temp = temp[:-1]
        temp = temp[::-1]
    else:
        print(0)
        break
    
            