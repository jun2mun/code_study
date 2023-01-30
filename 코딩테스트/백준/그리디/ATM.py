N = int(input()) #N(1 ≤ N ≤ 1,000)

queue = list(map(int,input().split()))
length = len(queue); total = 0
queue.sort()

for i in range(len(queue)):
    total += queue[i] * length
    length -= 1

print(total)