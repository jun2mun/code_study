answer = 0
def solution(begin, target, words):
    dfs(begin,words,0,target)
    print(answer)
    return answer

def compare(word,target):
    cnt = 0
    for x,y in zip(word,target):
        if x != y:
            cnt +=1
    if cnt == 1:
        return True

def dfs(begin,words,cnt,target):
    global answer
    if target == begin: # 종료 조건 (1) : 같아진 경우
        answer = cnt
        return
    else:
        if len(words) == 0:
            return
        for idx in range(len(words)):
            if compare(begin,words[idx]): # 재귀
                word = words[:idx] + words[idx+1:]
                dfs(words[idx],word,cnt+1,target) # 종료 조건에서 얻어냄
    

        

if __name__ == "__main__":
    begin = "hit"; target ="cog"; words=["hot", "dot", "dog", "lot", "log", "cog"]
    solution(begin,target,words)