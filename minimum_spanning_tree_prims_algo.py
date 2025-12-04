import heapq

def minimumCost(N, edges):
    adj = [[] for _ in range(N+1)]
    visited = [False]*(N+1)

    for v1, v2, cost in edges:
        adj[v1].append((cost, v2))
        adj[v2].append((cost, v1))

    total_weight = 0
    count = 0

    q = [(0, 1)]

    while q:
        weight, node = heapq.heappop(q)
        if visited[node] == True:
            continue
        visited[node] = True
        # heapq.heappush(q, (weight, node))

        total_weight += weight
        count += 1

        for wt, n in adj[node]:
            if not visited[n]:
                heapq.heappush(q, (wt, n))

    if count != N:
        return -1
    return total_weight
