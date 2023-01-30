# 2를 곱한다
# 1을 수의 가장 오른쪽에 추가한다.

A, B = map(int,input().split()) # (1 ≤ A < B ≤ 109
temp = B; cnt = 0; find = False
while True:
    if temp % 2 == 0 : 
        temp = temp//2
        cnt +=1
    else :
        if temp % 10 == 1: # 마지막 자리가 1일 경우
            if temp // 10 < A:
                break
            else:
                temp = temp // 10
                cnt +=1
        else:
            break


    if temp == A:
        find = True
        print(cnt +1)
        break

# 만들 수 잇는 경우
# 필요한 연산의 최솟값에 1을 더한 값

# 만들 수 없는 경우
if find == False:
    print(-1)

