def topoSort(V, edges):
    from collections import defaultdict

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * (V + 1)  
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)  

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i)

    stack.reverse()
    return stack
