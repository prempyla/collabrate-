def minCoins(value, coins):
    dp = {}
    res = solver(value, coins, dp)
    if res == float("inf"):
        return -1
    return res

def solver(value, coins, dp):
    if value < 0:
        return float("inf")
    if value == 0:
        return 0

    if value in dp:
        return dp[value]

    my_ans = float("inf")

    for coin in coins:
        small_ans = solver(value-coin, coins, dp)
        my_ans = min(my_ans, small_ans+1)

    dp[value] = my_ans
    return my_ans
