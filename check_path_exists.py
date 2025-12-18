def isSibling(n, x, y, edges):
    adj = [[] for _ in range(n)]
    visited = [False]*n
    lst = []

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node):
        if visited[node] == True:
            return 
        visited[node] = True
        lst.append(node)

        for neigh in adj[node]:
            if not visited[neigh]:
                dfs(neigh)

    dfs(x)
    if y in lst:
        return True
    return False
