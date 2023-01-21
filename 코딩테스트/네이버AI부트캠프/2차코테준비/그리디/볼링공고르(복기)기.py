
if __name__ == '__main__':
    N,M = map(int,input().split()) # N 볼링공 개수 M 공의 최대 무게
    balls = list(map(int,input().split()))
    balls.sort()
    total = len(balls); answer = 0

    for i in range(len(balls)-1):
        ball = balls[i]; count = 0
        for idx in range(i+1,len(balls)):
            if ball != balls[idx]:
                break
            else:
                count +=1
        print(total,count,i)
        answer += (total - count - i - 1)

    print(answer)

#### 리스트 크기가 10으로 M의 범위가 작으니 리스트를 생성해도 됨.