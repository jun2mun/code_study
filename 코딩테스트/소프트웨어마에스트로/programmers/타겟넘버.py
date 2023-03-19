
def dfs(numbers,visited,cur,target,cnt):
    ans = 0
    
    if cur == len(numbers):
        if cnt == target:
            return 1
        else:
            return 0
    else:
        for i in (-1,1):
            ans += dfs(numbers,visited,cur+1,target,cnt + numbers[cur] * i)

    return ans
    


def solution(numbers, target):
    visited = [False] * len(numbers) # 방문 확인
    answers = dfs(numbers,visited,0,target,0)
    print(answers)

solution([1,1,1,1,1],3)