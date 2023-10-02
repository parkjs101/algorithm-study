n = int(input())

arr = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
	for j in range(i):
		if arr[j] > arr[i] and dp[i] <= dp[j]: ##n = 5, arr = 1 3 2 3 1 인 경우 
			dp[i] = dp[j] + 1

print(max(dp))