import sys
sys.setrecursionlimit(10**6)

def frogJump(heights):
    dp = {}
    return solve(0, heights, dp)

def solve(index, heights, dp):
    if index >= len(heights)-1:
        return 0
    if index in dp:
        return dp[index]
    one_jump = abs(heights[index+1]-heights[index]) + solve(index+1, heights, dp)
    two_jump = float("inf")
    if index+2 < len(heights):
        two_jump = abs(heights[index+2]-heights[index]) + solve(index+2, heights, dp)
    dp[index] = min(one_jump, two_jump)
    
    return dp[index]
