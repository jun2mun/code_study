import heapq
# 이 문제는 heapq로만 풀어야 해결이 가능함. (시간 초과)
if __name__ == '__main__':
    # 가격의 최대
    N,K = map(int,input().split())
    diamonds = [] # 무게 / 가격
    bags = []
    for _ in range(N):
        heapq.heappush(diamonds,list(map(int,input().split()))) # ( min heap)
    for _ in range(K):
        bags += [int(input())]
    bags.sort() # 가방은 작은 순서대로 정렬(오름차순)

    answer = 0
    tmp_dia = []
    for bag in bags:
        # 넣을 다이아몬드가 있을 경우 iter
        while diamonds and bag >= diamonds[0][0]: # 다이아몬드가 가방에 들어갈 수 있을 경우 
            # 제일 비싼 보석이 root에 있어야 함
            heapq.heappush(tmp_dia,-heapq.heappop(diamonds)[1]) # (max heap)
        if tmp_dia:
            answer -= heapq.heappop(tmp_dia) # 다이아를 넣음 (- 이기때문에 -로 뺌)
        elif not diamonds: # 다이아 없으면 종료
            break
    print(answer)
            

