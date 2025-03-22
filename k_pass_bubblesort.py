n,k=map(int,input().split())
arr=list(map(int, input().split()))
for i in range(k):
    for j in range(1,n):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
print(*arr)
