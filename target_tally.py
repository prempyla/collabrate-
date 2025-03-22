def count_lesser_or_equal(arr,target):
    n=len(arr)
    left,right=0,n-1
    ans=-1

    while left<=right:
        mid = (left+right)//2
        if arr[mid] <= target:
            ans = mid
            left=mid+1
        else:
            right=mid-1
    return ans+1
# brute force code
# n=len(arr)
#     prefix=[0]*n
#     if arr[0]<=target:
#         prefix[0]=1
#     for i in range(1,n):
#         if arr[i]<=target:
#             prefix[i]=prefix[i-1]+1
#         else:
#             return prefix[i-1]
#     return prefix[n-1]
