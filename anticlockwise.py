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
