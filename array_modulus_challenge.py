n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
x=int(input())
total=0
for row in matrix:
    total+=sum(row)
if total%x==0:
    print(1)
else:
    print(0)
  
