def solve(n, edges):
    g = [[] for _ in range(n+1)]
    rg = [[] for _ in range(n+1)]  # reversed graph

    for a, b in edges:
        g[a].append(b)
        rg[b].append(a)

    def dfs(start, graph):
        visited = [False] * (n + 1)
        stack = [start]
        visited[start] = True

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return visited

    visited1 = dfs(1, g)
    if not all(visited1[1:]):
        return False

    visited2 = dfs(1, rg)
    if not all(visited2[1:]):
        return False

    return True
