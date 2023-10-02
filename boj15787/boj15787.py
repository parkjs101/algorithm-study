n, m = map(int, input().split())

arr = [[0 for _ in range(20)] for _ in range(n)] #사람이 타있으면 1 / 없으면 0
count = 0

for i in range(m): #m번의 명령 입력받고 수행
	order = list(map(int, input().split()))

	if order[0] == 1:
		arr[order[1]-1][order[2]-1] = 1

	elif order[0] == 2:
		arr[order[1]-1][order[2]-1] = 0

	elif order[0] == 3:
		arr[order[1]-1][-1] = 0
		for i in range(19):
			arr[order[1]-1][19-i] = arr[order[1]-1][18-i]
		arr[order[1]-1][0] = 0

	elif order[0] == 4:
		arr[order[1]-1][0] = 0
		for i in range(19):
			arr[order[1]-1][i] = arr[order[1]-1][i+1]
		arr[order[1]-1][-1] = 0

"""
record = []
for i in range(n):
	x = ''.join(str(arr[i]))
	if x not in record:
		count += 1
		record.append(x)

print(count)
"""

record = set()
for i in range(n):
	x = ''.join(str(arr[i]))
	if x not in record:
		count += 1
		record.add(x)

print(count)
