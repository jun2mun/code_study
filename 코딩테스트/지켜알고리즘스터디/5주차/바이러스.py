# 종료 조건
# 더이상 방문할 곳이 없을때

def DFS(Com_num):
    global virus_cnt
    visited[Com_num] = 1 #  현재 위치 방문 처리
    # 방문하지 않았고 + 연결되어 있는 노드인 경우

    
    for idx in range(1,Com_cnt+1):
        if Network[Com_num][idx] == 1 and visited[idx] != 1:
            virus_cnt += 1
            DFS(idx)


if __name__ == '__main__':
    virus_cnt= 1
    # 첫째 줄 (컴퓨터의 수 <= 100) 
    Com_cnt = int(input())
    # 둘째 줄 (네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수)
    Com_pair = int(input())
    # 이어서 아래는 // 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는
    # 컴퓨터 번호 쌍이 주어짐.
    
    # 방문여부
    visited = [0] * (Com_cnt+1)
    # 네트워크 상 연결 여부
    Network = [[0] * (Com_cnt +1) for _ in range(Com_cnt+1)]
    
    for _ in range(Com_pair):
        X,Y = map(int,input().split())
        Network[X][Y] = 1
        Network[Y][X] = 1

    DFS(1) # 1번 컴퓨터가 웜 바이러스 걸림.

    print(virus_cnt -1)