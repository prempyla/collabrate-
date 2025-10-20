def mazeObstacles(m, n, obstacleGrid):
    dp = {}
    mod = (10**9)+7
    if obstacleGrid[0][0] == 1:
        return 0
    if obstacleGrid[m-1][n-1] == 1:
        return 0
    return solve(m-1,n-1, obstacleGrid, dp, mod)

def solve(m, n, obstacleGrid, dp, mod):
    if m == 0 and n == 0:
        return 1
    if m < 0 or n < 0:
        return 0 
    if obstacleGrid[m][n] == 1:
        return 0

    if (m,n) in dp:
        return dp[(m,n)]

    dp[(m,n)] = (solve(m-1, n,obstacleGrid, dp, mod) + solve(m, n-1,obstacleGrid, dp, mod)) % mod

    return dp[(m, n)]
