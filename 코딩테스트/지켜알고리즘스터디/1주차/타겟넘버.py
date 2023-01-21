import sys
sys.setrecursionlimit(100000)
def dfs(target,numbers,visited,idx,cnt):
    answer = 0

    if not(False in visited): # 전부 방문하였을때,
        if cnt == target:
            return 1
        return 0
    if visited[idx] == False:
        visited[idx] = True
        answer += dfs(target,numbers,visited,idx+1,cnt + (numbers[idx] * -1))
        answer += dfs(target,numbers,visited,idx+1,cnt+ (numbers[idx]))
        visited[idx] = False

    return answer


def solution(numbers, target):

    visited = [False for _ in range(len(numbers))]
    answer = dfs(target,numbers,visited,idx=0,cnt=0)
    return answer