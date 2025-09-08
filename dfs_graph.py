def dfsOfGraph(n, edges):
    adj_lst = [[] for _ in range(n)]
    visited = [False] * n
    order = []

    for u,v in edges:
        adj_lst[v].append(u)
        adj_lst[u].append(v)

    def DFS(node):
        visited[node] = True
        order.append(node)
        for neighbor in adj_lst[node]:
            if not visited[neighbor]:
                DFS(neighbor)
    
    for item in range(n):
        if not visited[item]:
            DFS(item)

    # DFS(0)

    return order
