N = int(input())# 단어의 개수
words =[input() for _ in range(N)]
cnt = N
for word in words:
    alpahbets = []
    for alphabet in range(len(word)):
        if word[alphabet] in alpahbets:
            # 있으면 연속된 글자인지 확인
            if word[alphabet-1] == word[alphabet]:
                continue
            else:
                cnt -=1
                break             
        else:
            alpahbets.append(word[alphabet]) #없으면 추가

print(cnt)