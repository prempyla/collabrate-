n=int(input())
arr=list(map(int,input().split()))
total=0
for i in range(n):
    if i==0 or i%3==0:
        total+=arr[i]
print(total)
