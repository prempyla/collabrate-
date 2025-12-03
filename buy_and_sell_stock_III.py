def maxProfit(prices):
    n = len(prices)
    dp = {}
    return solve(0, 0, 0, n, dp)

def solve(i, buy, k, n, dp):
    if i >= n:
        return 0
    if (i, buy, k) in dp:
        return dp[(i, buy, k)]
    if buy == 0 and k <= 2:
        dp[(i, buy, k)] = max(solve(i+1, 1, k+1, n, dp) - prices[i], solve(i+1, 0, k, n, dp))
    elif buy == 1 and k <= 2:
        dp[(i, buy, k)] = max(solve(i+1, 0, k, n, dp) + prices[i], solve(i+1, 1, k, n, dp))
    else:
        return 0
        
    return dp[(i, buy, k)]
