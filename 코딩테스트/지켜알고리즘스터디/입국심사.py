def solution(n, times):
    times.sort() # 정렬
    start = 1; end = times[-1] * n # 최대 시간
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for refree in times:
            people += mid// refree
            if people > n:
                break        
        if people >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    
    return answer



if __name__ == "__main__":
    n = 6; times=[7,10]
    solution(n,times)