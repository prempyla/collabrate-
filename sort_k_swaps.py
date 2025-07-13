def bubbleSort(nums, k):
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(1,n):
            if nums[j] < nums[j-1]:
                count+=1
                nums[j],nums[j-1]=nums[j-1],nums[j]
    if count <= k:
        return True
    return False
