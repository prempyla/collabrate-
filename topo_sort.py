def topoSort(V, edges):
    adj = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    lst = []

    for u, v in edges:
        adj[u].append(v)

    def dfs(node):
        if visited[node] == True:
            return 
        visited[node] = True
        
        for neigh in adj[node]:
            if not visited[neigh]:
                dfs(neigh)
        lst.append(node)


    for i in range(1, V+1):
        if visited[i] == False:
            dfs(i)

    return lst[::-1]
