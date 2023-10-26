n, s = map(int, input().split())
li = list(map(int, input().split()))
isused = [0]*n
count = 0

def func1(d, l, index, sub_arr):
  global count
  if d == l:
    if sub_arr == s:
      count += 1
    return
  else:
    for i in range(index, n):
      if isused[i] == 1:
        continue
      else:
        sub_arr += li[i]
        isused[i] = 1
        func1(d+1, l, i+1, sub_arr)
        isused[i] = 0
        sub_arr -= li[i]

for i in range(1, n+1):
  sub_arr = 0
  func1(0, i, 0, sub_arr)

print(count)