def solution(brown, yellow):
    answer = []

    # 가로 세로 최소의 차이.
    for y in range(1,int(yellow**(1/2))+1):
        if yellow % y == 0:
            x = yellow // y
            if ( (x+2) * 2 + (y+2) *2  - 4  ) == brown:
                answer = [x+2,y+2]

    return answer

if __name__ == "__main__":
    brown = 10; yellow = 2
    print(solution(brown,yellow))
    pass