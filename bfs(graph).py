from collections import deque

def bfsOfGraph(n, edges, src):
    visited = [False]*n
    adj = [[] for _ in range(n)]
    bfs = []

    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    q = deque()
    q.append(src)
    visited[src] = True

    while q:
        node = q.popleft()
        bfs.append(node)

        for neigh in adj[node]:
            if not visited[neigh]:
                q.append(neigh)
                visited[neigh] = True

    return bfs
