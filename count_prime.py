n=(10**6)+1
isPrime=[True]*n
isPrime[0]=isPrime[1]=False
for i in range(2, int(n**0.5)+1):
    if isPrime[i]==False:
        continue
    for j in range(i*2,n,i):
        isPrime[j]=False

prefix=[0]*n
count=0
for i in range(1,n):
    if isPrime[i]:
        count+=1
    prefix[i]=count
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    print(prefix[r]-prefix[l-1])
