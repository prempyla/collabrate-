def minDistance(word1, word2):
    n=len(word1)
    m=len(word2)
    dp = {}
    return solve(word1, word2, n, m, dp)

def solve(word1, word2, n, m, dp):
    if (n,m) in dp:
        return dp[(n,m)]
    if n == 0:
        return m
    if m == 0:
        return n
    if word1[n-1] == word2[m-1]:
        return solve(word1, word2, n-1, m-1, dp)
    insert = 1 + solve(word1, word2, n, m-1, dp)
    delete = 1 + solve(word1, word2, n-1, m, dp)    
    replace = 1 + solve(word1, word2, n-1, m-1, dp) 

    dp[(n,m)] = min(insert, delete, replace)
    
    return dp[(n,m)]
