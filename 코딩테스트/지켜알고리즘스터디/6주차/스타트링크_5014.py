from collections import deque
def bfs(start,end,F):
    queue = deque()
    queue.append([start,0])
    visited = [False] * (F+1)
    visited[start] = True
    while queue:
        cur,cnt = queue.popleft()
        if cur == end:
            # 반환할때 현재 몇번 버튼 눌렀는지 알아야함
            return cnt
        for i in (cur+U, cur-D): #U만큼 위로 or D만큼 아래로
            if 1 <= i <= F and not visited[i]:
                visited[i] = True
                queue.append([i,cnt+1])
        
    return 'use the stairs' # 갈수 없을 경우

if __name__ == '__main__':
    F,S,G,U,D = map(int,input().split())
    print(bfs(S,G,F))
