import sys
from collections import deque

T = int(input())
for i in range(T):
	m, n, k = map(int, input().split())
	board = [[0]*m for _ in range(n)]
	vis = [[0]*m for _ in range(n)]
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	dq = deque([])
	w = 0

	for i in range(k):
		x, y = map(int, sys.stdin.readline().split())
		board[y][x] = 1
	
	for i in range(n):
		for j in range(m):
			if board[i][j] != 1 or board[i][j] == vis[i][j]:
				continue
			else:
				vis[i][j] = 1
				dq.append((j,i))
				w += 1
				while dq:
					cx = dq[0][0]
					cy = dq[0][1]
					dq.popleft()
					for k in range(4):
						nx = cx + dx[k]
						ny = cy + dy[k]
						if nx<0 or nx>=m or ny<0 or ny>=n:
							continue
						elif board[ny][nx] != 1 or board[ny][nx] == vis[ny][nx]:
							continue
						else:
							dq.append((nx, ny))
							vis[ny][nx] = 1

	print(w)