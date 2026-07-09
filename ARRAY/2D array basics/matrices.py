matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    
]
for i in range(len(matrix)): ##rows=5
    for j in range(len(matrix[0])): ##colums=3 → based on columns it will see how many are columns are there and identify
        print(matrix[i][j], end=' ')
    print()


























# print("row and column is:\n",matrix[1][2])  ##matrix[row][column]
# print("length of matrix is:\n",len(matrix))
# print("length of",matrix[0],"is:\n",len(matrix[0]))
# print("length of",matrix[1],"is:\n",len(matrix[1]))
# print("length of",matrix[2],"is:\n",len(matrix[2]))
