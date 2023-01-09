# 문제는 완전탐색인데, DFS로 풀고 싶어서 풀었음.

answer = 0; cnt = 0
import sys
sys.setrecursionlimit(100000)
def dfs(word,target):
    global answer
    global cnt
    dict_ = ['A','E','I','O','U']
    if word == target:
        answer = cnt
    if len(word) == len(dict_):
        return 
    for key in dict_:
        cnt +=1
        dfs(word+key,target)
        #if answer != None:
        #    return answer
    

def solution(word):
    dfs('',word)
    return answer

if __name__ == "__main__":
    word = "AAAAE"
    word = "AAAE"
    word = "I"
    word = "EIO"
    solution(word)
    pass
