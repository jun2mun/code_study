
if __name__ == '__main__':
    # 1 1 2 3 9
    
    N = int(input())
    coins = list(map(int,input()))
    coins.sort()
    target = 1

    for x in coins:
        if target < x:
            break
        target +=x
