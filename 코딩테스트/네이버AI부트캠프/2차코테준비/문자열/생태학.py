import sys
answer = dict()
cnt = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if tree == '':
        break
    if tree in answer: # dict key 기준으로 찾기.
        answer[tree] +=1
    else:
        answer[tree] = 1
    cnt +=1

answer = dict(sorted(answer.items()))
for idx in answer:
    a = answer[idx]
    per = (a / cnt * 100)
    
    print("%s %.4f" %(idx, per)) # round 쓰면 안됨 사사오입이여서 ㅎㅎ