import sys
n= int(input())

cost = [[0] for i in range(n)]

for i in range(n):
    cost[i] = list(map(int, sys.stdin.readline().split()))

sum = [[0, 0, 0] for i in range(n)]

for i in range(n):
    if i == 0:
        sum[i] = [cost[i][0],  cost[i][1],  cost[i][2]]
    else:
        sum[i][0] = min(sum[i-1][1], sum[i-1][2]) + cost[i][0]
        sum[i][1] = min(sum[i-1][0], sum[i-1][2]) + cost[i][1]
        sum[i][2] = min(sum[i-1][0], sum[i-1][1]) + cost[i][2]

print(min(sum[-1]))