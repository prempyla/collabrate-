def uniquePaths(m , n):
    dp = {}
    return solve(m, n, dp)

def solve(m, n, dp):
    if m<1 or n<1:
        return 0
    if m==1 and n==1:
        return 1
    if (m, n) in dp:
        return dp[(m, n)]
    
    dp[(m, n)] = solve(m-1, n, dp) + solve(m, n-1, dp)

    return dp[(m,n)]
