from collections import deque

n, m, v = map(int, input().split())
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

vis_dfs = [0]*(n+1)
vis_bfs = [0]*(n+1)

for i in range(m):
	x, y = map(int, input().split())
	arr[x][y] = 1
	arr[y][x] = 1

def dfs(v):
	vis_dfs[v] = 1
	print(v, end= " ")
	for i in range(1, n+1):
		if vis_dfs[i] == 0 and arr[v][i] == 1:
			dfs(i)

def bfs(v):
	vis_bfs[v] = 1
	q = deque()
	q.append(v)
	while q:
		b = q.popleft()
		print(b, end=" ")
		for i in range(1, n+1):
			if vis_bfs[i] == 0 and arr[b][i] == 1:
				q.append(i)
				vis_bfs[i] = 1

dfs(v)
print()
bfs(v)


