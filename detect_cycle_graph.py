def isCyclic(n, edges):
    adj = [[] for _ in range(n)]
    visited = [False] * n
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node, parent):
        visited[node] = True
        for neigh in adj[node]:
            if not visited[neigh]:
                if dfs(neigh, node):  
                    return True
            elif neigh != parent:
                return True
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False
