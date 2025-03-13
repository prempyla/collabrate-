def count_lesser_or_equal(arr,target):
    # write your code here
    n=len(arr)
    prefix=[0]*n
    if arr[0]<=target:
        prefix[0]=1
    for i in range(1,n):
        if arr[i]<=target:
            prefix[i]=prefix[i-1]+1
        else:
            return prefix[i-1]
    return prefix[n-1]
