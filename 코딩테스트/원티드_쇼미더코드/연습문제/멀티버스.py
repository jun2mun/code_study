# 두개씩 비교 (world 간 비교)
def compare(x,y):
    pass
# world간 행성2개씩 비교.

if __name__ == '__main__':
    M, N = map(int,input().split())
    #worlds = [list(map(int,input().split())) for _ in range(M)]
    worlds = [[20, 10, 30], [10, 20, 60], [80, 25, 79], [30, 50, 80], [80, 25, 81]]

    # 순차 비교 (O n^2)
    for x in range(len(worlds)-1):
        for y in range(x+1,len(worlds)-1):
            compare(x,y)
            print(worlds[x],worlds[y])
    
    #pass