n=int(input())
matrix=[]
for _ in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
total = 0
for i in range(n):
    total+=matrix[0][i]
if n >1:
    for i in range(n):
        total+=matrix[n-1][i]
for j in range(1,n-1):
    total+=matrix[j][n-j-1]
print(total)
