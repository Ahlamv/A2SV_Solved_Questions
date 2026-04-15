class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        cols=len(matrix[0])
        res=[[0]* row for k in range(cols)]
        for i in range(cols):
            for j in range(row):
               res[i][j]=matrix[j][i]
        return res