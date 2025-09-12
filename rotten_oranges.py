from collections import deque

def orangesRotting(grid):
    # Write your code here
    q = deque()
    n=len(grid)
    m=len(grid[0])
    time=0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append([i,j,0])
    
    while len(q)>0:
        r,c,t = q.popleft()
        
        if t>time:
            time=t

        if r-1>=0 and grid[r-1][c]==1:
            q.append([r-1,c,t+1])
            grid[r-1][c]=2
        
        if r+1<n and grid[r+1][c]==1:
            q.append([r+1,c,t+1])
            grid[r+1][c]=2

        if c-1>=0 and grid[r][c-1]==1:
            q.append([r,c-1,t+1])
            grid[r][c-1]=2

        if c+1<m and grid[r][c+1]==1:
            q.append([r,c+1,t+1])
            grid[r][c+1]=2

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return -1
    return time
