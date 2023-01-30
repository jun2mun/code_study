N = int(input()) # 도시의 개수
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))
total_cost = 0;find = False

min_price = roads[0] * costs[0]
lowest = sorted(costs[:-1])[0]


for i in range(len(costs)-1):
    if find == True:
        total_cost += lowest * roads[i]
        continue
    else:
        if costs[i] == lowest:
            find = True
            total_cost += lowest * roads[i]
        else:
            total_cost += costs[i] * roads[i]


print(total_cost)

