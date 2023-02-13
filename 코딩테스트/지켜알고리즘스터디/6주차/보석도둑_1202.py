import heapq
# 이 문제는 heapq로만 풀어야 해결이 가능함.
if __name__ == '__main__':
    # 가격의 최대
    N,K = map(int,input().split())
    diamonds = [] # 무게 / 가격
    bags = []
    for _ in range(N):
        heapq.heappush(diamonds,list(map(int,input().split())))
    for _ in range(K):
        bags += [int(input())]
    bags.sort()

    answer = 0
    tmp_dia = []
    for bag in bags:
        while diamonds and bag >= diamonds[0][0]:
            heapq.heappush(tmp_dia,-heapq.heappop(diamonds)[1])
        if tmp_dia:
            answer -= heapq.heappop(tmp_dia)
        elif not diamonds:
            break
    print(answer)
            

# 99 65 23 50
# 2  6  1  4

# 2 5 10
# 99 50 65 이렇게 하면 비교을 많이 해야함.
# 
#   


