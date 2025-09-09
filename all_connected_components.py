def connectedComponents(n, edges):
    adj = [[] for _ in range(n)]
    visited = [False] * n
    lst = []

    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node, lst):
        if visited[node] == True:
            return
        else:
            visited[node] = True
            lst.append(node)
            for neigh in adj[node]:
                dfs(neigh, lst)
    
    for item in range(n):
        if visited[item] == False:
            new_lst = []
            dfs(item, new_lst)
            lst.append(new_lst)
    
    return lst
