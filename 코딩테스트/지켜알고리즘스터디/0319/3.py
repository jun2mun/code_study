from collections import deque
import sys
sys.setrecursionlimit(10000000)
result = []
def dfs(gems : deque,categories,start,end):
    global result
    if len(set(gems)) == len(categories): # 보석 종류별로 하나씩 있을 경우
        result.append([start+1,end+1]) # 인덱스 값 추출
    if len(set(gems)) < len(categories): # 보석 종류별로 없을 경우 종료
        return

    value =gems.pop() # 오른쪽 pop
    dfs(gems,categories,start,end-1)
    gems.append(value)
    
    gems.popleft() # 왼쪽 pop
    dfs(gems,categories,start+1,end)
    gems.appendleft(value)
    
def solution(gems):
    #answer = []
    gems = deque(gems)
    
    categories = set(gems)
    #print(categories)
    dfs(gems,categories,0,len(gems)-1)
    #print(sorted(result,key=lambda x: abs(x[1]-x[0])) )
    

    return sorted(result,key=lambda x: abs(x[1]-x[0]))[0]
############################################

def real_solution(gems):
    N = len(gems)
    answer = [0,N-1]
    kind = len(set(gems))
    dic = {gems[0] :1,}
    start,end = 0,0 # 투 포인터
    while start < N and end < N:
        if len(dic) < kind: #보석 종류 미달시
            end +=1
            if end == N:
                break
            dic[gems[end]] = dic.get(gems[end],0) + 1 # 
        else: # 개수 채웠을 경우 , ans 값 최소화 가능한지 여부 확인
            if (end - start + 1) < (answer[1] - answer[0] + 1):
                answer = [start,end] # 갱신
            if dic[gems[start]] == 1:
                del dic[gems[start]] # 개수 다운(갱신)
            else:
                dic[gems[start]] -= 1
            start +=1 # start 를 비움
    answer[0] += 1
    answer[1] += 1
    return answer
            

