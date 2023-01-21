def solution():
    # 첫 번째 장애물은 항상 석순
    # 종유석과 석순이 번갈아가면서 등장 
    # N 만큼 경로 선택 가능

    # 석순의 경우 : (H -1) 만큼 방해
    # 종유석의 경우 : (H-1) 만큼 방해
    # 종유석과 석순이 번갈아 나오는 것을 특징으로 (Graph 그려서 풀기에 많음)


    pass

if __name__ == '__main__':
    N,H = map(int,input().split()) # N은 항상 짝수 (N길이 미터, H 높이 미터)
    
    gate = []
    for _ in range(N):
        gate.append(int(input()))

    # 1구간 : +=1 개수
    # 2구간 : +=1 개수
    # 3구간 : +=1 개수
    # (0,1) (1,H-3) (2,4)
    routes = [0 for _ in range(H)] # 라인 충돌 개수

    for x in range(N):
        석순 = True; 종유석 = False
        if x % 2 == 0:
            석순 = True; 종유석 = False
        if x % 2 == 1:
            석순 = False; 종유석 = True

        if 석순 == True:
            for i in range(gate[x]):
                routes[i] +=1
        if 종유석 == True:
            for i in range(-1,-gate[x]-1,-1):
                routes[i] +=1
    
    count = 0        
    routes.sort() # 정렬
    for route in routes:
        if routes[0] != route:
            break
        count +=1

    print(routes[0],count)
