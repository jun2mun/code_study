def _sum(idx):
    cnt = 0
    for num in range(idx):
        cnt += num
    return cnt


if __name__ == '__main__':
    num_list = []; answer = 0
    num = int(input())
    for i in range(1,int(num ** (1/2))+1):
        if num % i == 0:
            num_list = num_list + [i] + [num//i]
    
    num_list.sort()

    for idx in range(len(num_list)):
        answer += _sum(idx)
    
    print(answer)

#############################
# 아래 알고리즘이 정답 #
n = int(input())

sum = 0

for i in range(1, n+1) :
  sum += (n//i)*i
print(sum)
