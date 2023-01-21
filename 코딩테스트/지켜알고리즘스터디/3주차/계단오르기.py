# 규칙
# 1번 . 계단은 한번에 한계단 or 두 계단
# 2번 . 연속된 세 개의 계단을 모두 밟아서는 안된다. (시작점 제외)
# 3번 . 마지막 도착 계단은 반드시 밟아야 한다.

def dfs(idx,cost,conn):
    global answer
    if conn >= 3:
        return
    if idx == N-1:
        answer = max(answer,cost)
    for i in range(1,3):
        if idx + i > N-1:
            return
        if idx == -1:
            dfs(idx+i,cost + score_list[idx+i],conn+1)
            continue
        elif i == 1:
            dfs(idx+i,cost + score_list[idx+i],conn+1)
        else:
            dfs(idx+i,cost + score_list[idx+i],1)

if __name__ == '__main__':
    score_list = []; answer =0
    N = int(input()) # 계단의 개수 <= 300
    for idx in range(N): # 점수 <= 10,000
        score_list.append(int(input()))
    

    dfs(-1,0,0)
    print(answer)

    
# [0,1] [0,2] [1,2] [1,3] [2,3] [2,4]
# [3,4] [3,5] [4,5] [4,6]