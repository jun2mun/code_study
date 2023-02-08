if __name__ == '__main__':
    N,M = map(int,input().split())
    trees = list(map(int,input().split()))

    start, end = 1, max(trees) #이분탐색 검색 범위 설정

    while start <= end:
        mid = (start + end) // 2

        result = 0
        for i in trees:
            if i  >= mid:
                result += (i-mid)
        
        if result >= M:
            start = mid +1
        
        elif result < M:
            end = mid - 1
    
    print(end) # end가 최대의 절단 길이 임으로 end 사용
