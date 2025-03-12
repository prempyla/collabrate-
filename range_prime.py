n=(10**6)+1
isPrime=[True]*n
isPrime[0]=isPrime[1]=False
for i in range(2, int(n**0.5)+1):
    if isPrime[i]==False:
        continue
    for j in range(i*2,n,i):
        isPrime[j]=False

ans=0
l,r=map(int,input().split())
for i in range(l,r+1):
    if isPrime[i]:
        ans+=1

print(ans)
