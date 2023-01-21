if __name__ == '__main__':
    N = int(input()) # 모험가의 수
    horrors = list(map(int,input().split()))
    horrors.sort(reverse=True)
    horror = horrors[:]; cnt = 0
    while True:
        print(horror)
        if len(horror) == 0:
            break
        if horror[0] > len(horror):
            break
        horror = horror[horror[0]:]
        cnt +=1
    print(cnt)


    # 위에는 최소로 구함.