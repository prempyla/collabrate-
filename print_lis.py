def getLIS(nums):
    n = len(nums)
    dp = [1]*n
    last_ind = 0
    maxi = 0
    ind = [-1]*n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j]+1 :
                dp[i] = 1+dp[j]
                ind[i] = j
        if dp[i] > maxi:
            maxi = dp[i]
            last_ind = i

    lis = []
    while last_ind != -1:
        lis.append(nums[last_ind])
        last_ind = ind[last_ind]

    return lis[::-1]
