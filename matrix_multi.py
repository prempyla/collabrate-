# Matrix multiplication
matrix1=[]
for i in range(3):
    row=list(map(int, input().split()))
    matrix1.append(row)
# print(matrix)
matrix2=[]
for i in range(3):
    row=list(map(int, input().split()))
    matrix2.append(row)
# print(matrix2)

matrix=[[0 for _ in range(3)] for _ in range(3)]
# print(matrix)

for i in range(3):
    for j in range(3):
        for k in range(3):
            matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for ele in matrix:
    print(*ele)

