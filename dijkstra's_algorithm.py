import heapq

def shortestPaths(n, src, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = [float("inf")]*n
    dist[src] = 0
    pq = [(0,src)]

    while pq:
        curr, u = heapq.heappop(pq)
        if curr > dist[u]:
            continue
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
            
    return dist
