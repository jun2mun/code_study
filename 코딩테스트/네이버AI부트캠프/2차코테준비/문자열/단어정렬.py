import sys
n = int(sys.stdin.readline())
words = {}
for _ in range(n):
    word = sys.stdin.readline().strip()
    id = len(word)
    if not id in words:
        words[id] = set()
    words[id].add(word)


for i in sorted(words.keys()):
    for word in sorted(words[i]):
        print(word)