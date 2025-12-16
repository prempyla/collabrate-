import heapq

def shortestPaths(n, src, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  

    dist = [float('inf')] * n
    dist[src] = 0

    pq = [(0, src)]  

    while pq:
        curDist, node = heapq.heappop(pq)

        if curDist > dist[node]:
            continue

        for nei, weight in graph[node]:
            newDist = curDist + weight
            if newDist < dist[nei]:
                dist[nei] = newDist
                heapq.heappush(pq, (newDist, nei))

    return [d if d != float('inf') else -1 for d in dist]
