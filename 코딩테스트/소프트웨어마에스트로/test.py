from collections import deque
def dfs(gems :deque,categories,start,end,pos):
    answer = []

    if len(set(gems)) == len(categories):
        return [[start,end]]
            
    element = gems.pop()
    answer += dfs(gems,categories,start,end-1,'right')
    gems.append(element)

    element = gems.popleft()
    answer += dfs(gems,categories,start+1,end,'left')
    gems.appendleft(element)


    
    return answer
    
def solution(gems):
    answer = []
    gems = deque(gems)
    categories = set(gems)
    print(categories)

    print(dfs(gems,categories,0,len(gems)-1,None))

    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])