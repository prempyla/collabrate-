def findScoreSum(nums):
    n=len(nums)
    total = 0
    for i in range(n):
        for j in range(i,n):
            if i < j and nums[i]==nums[j]:
                total+=(j-i)
    return total
