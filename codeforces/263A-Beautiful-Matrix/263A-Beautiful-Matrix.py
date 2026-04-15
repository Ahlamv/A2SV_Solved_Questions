matrix=[list(map(int, input().split())) for _ in range(5)]
for i in range(len(matrix)):
  for j in range(len(matrix)):
    if matrix[i][j]==1:
      print(abs(i-2)+abs(j-2))