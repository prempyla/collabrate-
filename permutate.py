def permute(nums):
    result = []
    def helper(start):
        if start == len(nums):
            result.append(nums[:])
            return 
        for i in range(start,len(nums)):
            nums[i],nums[start]=nums[start],nums[i]
            helper(start+1)
            nums[i],nums[start]=nums[start],nums[i]

    helper(0)
    return result
