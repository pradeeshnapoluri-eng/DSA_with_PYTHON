# matrix=[
#     [1,1,1],
#     [1,1,0],
#     [1,1,1],
#     [1,1,1]
# ]
# zero_location=[]
# ##step1
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==0:
#             zero_location.append((i,j))
# ##step2
# for row,col in zero_location:
#     for a in range(len(matrix[0])):  ##for col it should know the rows.so any index num should add
#         matrix[row][a]=0
#     for b in range(len(matrix)):
#         matrix[b][col]=0

# for result in matrix:
#     print(result)

print("--------own practice--------")
matrix=[
    [0,1,1],
    [1,1,1],
    [1,1,1]
]
store_loc=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            store_loc.append((i,j))

for row,col in store_loc:
    for x in range(len(matrix[0])): ##for iteration of the column we need [0] in row.
        matrix[row][x]=0
    for y in range(len(matrix)):
        matrix[y][col]=0
for z in matrix:
    print(z)