# Your code here
m,n=map(int, input().split())
matrix=[]
for i in range(m):
    a=list(map(int,input().split()))
    matrix.append(a)
q=int(input())
for i in range(q):
    k=int(input())
    add=0
    for i in range(m):
        for j in range(n):
            if i+j==k:
                add+=matrix[i][j]
    print(add)
