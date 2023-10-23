tc = int(input())

for _ in range(tc):
	n, angle = map(int, input().split())
	m = n//2
	angle = (angle//45)%8
	arr = []
	
	for _ in range(n):
		arr.append(list(map(int, input().split())))

	for _ in range(angle): #각도만큼 반복
		newarr = [[0 for _ in range(n)] for _ in range(n)]
		for i in range(n):
			for j in range(n):
				if i == j:
					newarr[i][m] = arr[i][j]
				elif j == m:
					newarr[i][n-i-1] = arr[i][j]
				elif i+j == n-1:
					newarr[m][j] = arr[i][j]
				elif i == m:
					newarr[j][j] = arr[i][j]
				else:
					newarr[i][j] = arr[i][j]

		arr = [a[:] for a in newarr]

	for i in range(n):
		print(" ".join(map(str,arr[i])))