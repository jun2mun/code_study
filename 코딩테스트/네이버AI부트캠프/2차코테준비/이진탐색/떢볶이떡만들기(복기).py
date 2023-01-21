
if __name__ == '__main__':
    N, M = map(int,input().split())
    dducks = list(map(int,input().split()))
    dducks.sort(reverse=True); total = 0
    for duck in dducks:
        total += duck
    start = 0; end = dducks[0]
    while True:
        mid = (start + end) // 2

        target = total - mid * M

        if target < M :
            start = mid
        elif target > M:
            end = mid
        elif target == M:
            answer = mid
        elif start == end:
            pass

