N = int(input())
words = []
for _ in range(N):
    words += [int(input())]

words.sort(reverse=True)

k = 1
answer = -1
for i in range(len(words)):
    answer = max(answer,words[i]*k)
    k +=1
print(answer)