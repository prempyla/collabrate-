def merge(arr1,arr2):
    x=len(arr1)
    y=len(arr2)
    i=0
    j=0
    merged=[]
    while i<x or j<y:
        if i>=x:
            merged.append(arr2[j])
            j+=1
        elif j>=y:
            merged.append(arr1[i])
            i+=1
        elif arr1[i]<=arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    return merged

n,m=map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
even1=[]
odd1=[]
even2=[]
odd2=[]
for val in arr1:
    if val%2==0:
        even1.append(val)
    else:
        odd1.append(val)

for val in arr2:
    if val%2==0:
        even2.append(val)
    else:
        odd2.append(val)

ans=[]
ans.extend(merge(even1,even2))
ans.extend(merge(odd1,odd2))
print(*ans)

