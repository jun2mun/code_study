from collections import deque
def solution():
    find = False
    # BFS 로
    while not_visited: #  전부 방문시
        nx,ny = not_visited.popleft()
        #print(nx,ny)
        for x,y in zip(dx,dy):
            if 0<= nx+x <= length-1 and 0<= ny+y <=length-1:
                if graph[nx+x][ny+y] != 0:
                    continue
                elif nx+x == target_night[0] and ny+y == target_night[1]:
                    graph[nx+x][ny+y] = graph[nx][ny] + 1
                    return graph[target_night[0]][target_night[1]]-1
                else:
                    graph[nx+x][ny+y] = graph[nx][ny] + 1
                    not_visited.append([nx+x,ny+y])
            #print(not_visited)
    return 0

if __name__ == '__main__':
    N = int(input()) # 테스트 케이스의 개수
    
    # 이동 가능 방법 표시
    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [2,1,-1,-2,-2,-1,1,2]
    
    for _ in range(N):
        length = int(input()) # 체스판 한 변의 길이 ㅇ(4 <= I <= 300)
        cur_night = list(map(int,(input().split()))) # 현재 나이트가 있는 칸
        target_night = list(map(int,(input().split()))) # 현재 나이트가 있는 칸
        graph = [[0 for _ in range(length)] for _ in range(length)]; graph[cur_night[0]][cur_night[1]] = 1
        not_visited = deque(); not_visited.append((cur_night)) # 초기 설정
        print(solution())
    