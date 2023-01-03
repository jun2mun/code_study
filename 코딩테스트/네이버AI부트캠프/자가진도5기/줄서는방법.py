import math
def solution(n, k):
    line = [i for i in range(1,n+1)] # 초기 줄
    answer = []
    k -=1
    
    while line:
        a = k // math.factorial(n-1)
        answer.append(line[a])
        del line[a]

        k = k % math.factorial(n-1)
        n-=1


    return answer


if __name__ == '__main__':
    n = 3; k = 5
    solution(n,k)
    pass
