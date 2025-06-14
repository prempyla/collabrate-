def rob(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    
    def rob_linear(houses):
        prev1, prev2 = 0, 0
        for money in houses:
            temp = prev1
            prev1 = max(prev1, prev2 + money)
            prev2 = temp
        return prev1
    
    case1 = rob_linear(nums[:-1])
    case2 = rob_linear(nums[1:])
    
    return max(case1, case2)
n = int(input())
nums = list(map(int, input().split()))
print(rob(nums))
