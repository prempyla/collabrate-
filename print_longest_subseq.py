def getLIS(nums):
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_len = -1
    last_ind = -1
    for i in range( n):
        for j in range(i):
            if (nums[j] < nums[i] and dp[i] < dp[j]+1):
                dp[i] = dp[j]+1
                prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            last_ind = i

    lis = []
    while last_ind != -1:
        lis.append(nums[last_ind])
        last_ind = prev[last_ind]
    return lis[::-1]
