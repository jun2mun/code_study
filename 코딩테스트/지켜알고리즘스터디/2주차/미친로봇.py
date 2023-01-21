input_lst = list(map(int, input().split()))
n = input_lst[0]
dir_lst = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# 이동할 수 있는 방향값
move_lst = []
# 이동할 수 있는 방향에 대한 확률값
per = []

for i in range(1, len(input_lst)):
    if input_lst[i] != 0:
        move_lst.append(dir_lst[i - 1])
        per.append(input_lst[i] / 100)

visited = [(14, 14)]
ans = 0


def dfs(x, y, total):
    global ans
    if len(visited) == n + 1:
        ans += total
        return

    # 이동할 수 있는 좌표에 대해서만 탐색을 진행함
    for i in range(len(move_lst)):
        nx = x + move_lst[i][0]
        ny = y + move_lst[i][1]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, total * per[i])
            visited.pop()


dfs(14, 14, 1)
print(ans)