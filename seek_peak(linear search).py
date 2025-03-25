n,k=map(int,input().split())
arr=list(map(int, input().split()))
sub=[]
for i in range(n):
    for j in range(i,n):
        ans = arr[i:j+1]
        l=len(ans)
        if l==k:
            sub.append(sum(ans))
print(max(sub))
