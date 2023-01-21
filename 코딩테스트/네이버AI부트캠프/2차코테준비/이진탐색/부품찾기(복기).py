
if __name__ == '__main__':
    N = int(input())
    부품_리스트 = list(map(int,input().split()))
    M = int(input())
    부품 = list(map(int,input().split()))

    부품_리스트.sort()
    부품.sort()

    answer = []

    for i in 부품:
        if i in 부품_리스트:    
            answer.append(True)
        else:
            answer.append(False)
    
    print(answer)

