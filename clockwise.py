n, m = map(int, input().split())
mat=[]
for _ in range(n):
    lst=list(map(int, input().split()))
    mat.append(lst)

matrix=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(0)
    matrix.append(l)

for i in range(n):
    for j in range(m):
        matrix[j][i]=mat[i][j]

for row in matrix:
    row.reverse()

for i in matrix:
    print(" ".join(map(str, i)))
