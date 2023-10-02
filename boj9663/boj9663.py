n = int(input())
isused_m = [0]*40 
isused_x_y = [0]*40
isused_y_x = [0]*40
count = 0

def func1(k):
	global count
	if k == n:
		count += 1
		return
	else:
		for i in range(n):
			if isused_m[i] or isused_x_y[k-i+n-1] or isused_y_x[k+i]:
				continue
			isused_m[i] = 1
			isused_x_y[k-i+n-1] = 1
			isused_y_x[k+i] = 1
			func1(k+1)
			isused_m[i] = 0
			isused_x_y[k-i+n-1] = 0
			isused_y_x[k+i] = 0

func1(0)
print(count)


	