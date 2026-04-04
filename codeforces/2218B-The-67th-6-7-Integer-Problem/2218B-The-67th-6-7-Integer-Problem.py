t=int(input())
for i in range(t):
  arr = list(map(int, input().split()))
  arr.sort()
  for i in range(len(arr)-1):
    arr[i] *= -1
  print(sum(arr))