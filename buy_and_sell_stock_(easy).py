def maxProfit(prices):
    n = len(prices)
    mini = prices[0]
    profit = 0
    for i in range(1,n):
        profit = max(profit, prices[i]-mini)
        mini = min(prices[i], mini)
    return profit
