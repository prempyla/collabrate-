def maxSumDivThree(nums):  
    dp = [0, float('-inf'), float('-inf')]  
    
    for num in nums:  
        temp = dp[:]  
        for r in temp:  
            if r != float('-inf'):  
                dp[(r + num) % 3] = max(dp[(r + num) % 3], r + num)  
    
    return dp[0]
