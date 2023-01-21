from collections import deque
def flood(waters):
    # 물 좌표 리스트
    # 동서남북 퍼질수 있는지 확인
    # 가능시 물 시작 지점 제거, 나머지 퍼지는 장소 queue에 저장
    pass

def solution():
    pass

if __name__ == '__main__':
    R, C = map(int,input().split())
    graph = [list(input()) for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1); sx,sy,Dx,Dy,wx,wy = 0,0,0,0,0,0
    waters = []

    for i in range(R):
        for j in range(C):
            if graph[i][j] == "S":
                sx, sy = i, j # 스타트 지점.
            elif graph[i][j] == "D":
                Dx,Dy = i, j # 도착 지점
            elif graph[i][j] == "*":
                wx,wy = i, j # 물 지점

    
    for x,y in zip(dx,dy):
        nx,ny = wx+x,wy+y
        if 0<= nx < R and 0<= ny < R and (visited[nx][ny] != True) and graph[nx][ny] == '.':
            waters.append([nx,ny])
            visited[nx][ny] = True # 다음번에 갈 수 없는 곳이기에 방문처리
    
    for x,y in zip(dx,dy):
        nx,ny = sx+x,sy+y
        if 0<= nx < R and 0<= ny < R and (visited[nx][ny] != True):
            visited[nx][ny] = True # 방문  위치 방문처리




    
    solution()