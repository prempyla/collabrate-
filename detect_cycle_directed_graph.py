def isCyclic(n, edges):
    from collections import defaultdict

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * n
    recStack = [False] * n

    def dfs(node):
        visited[node] = True
        recStack[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recStack[neighbor]:
                return True

        recStack[node] = False
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return True

    return False
