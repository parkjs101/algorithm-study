n = int(input())

arr = [] #지역의 정보
hmax = 1
hmin = 100
max_count = 1 #물에 잠기는 곳의 수

for i in range(n):
	temp = list(map(int, input().split()))
	hmax = max(max(temp), hmax)
	hmin = min(min(temp), hmin)
	arr.append(temp)

for i in range(hmin, hmax):      # phase
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	q = []
	visited = set()  
	count = 0

	for j in range(n):
		for k in range(n):

			if arr[j][k] > i and ((j,k) not in visited):
				q.append([j,k])
				visited.add((j,k))

				while q:
					y = q[-1][0]
					x = q[-1][1]
					q.pop()
					for l in range(4):
						cy = y + dy[l]
						cx = x + dx[l]
						if cx >= n or cx < 0 or cy >= n or cy < 0 or arr[cy][cx] <= i:
							continue
						elif (cy, cx) in visited:
							continue
						else:
							q.append([cy, cx])
							visited.add((cy,cx))

				count += 1

			else:
				continue
	
	max_count = max(max_count, count)

print(max_count)