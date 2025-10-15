def convertToAdjList(n, edgeList):
    # write your code here
    adj = [[]for _ in range(n)]

    for u,v in edgeList:
        adj[u].append(v)
        adj[v].append(u)

    return adj
