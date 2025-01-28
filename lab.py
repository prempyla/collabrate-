# write a function code to find if target is present
# in range [i,j] or not. (0<=i<=j<=N-1)
# return true or false

def find(lst,target,i,j):
    lo=i
    hi=j
    while lo<=hi:
        mid=(lo+hi)//2
        value=lst[mid]
        if value==target:
            return True
        if target<mid:
            hi=mid-1
        elif target>mid:
            lo=mid+1
    return False
