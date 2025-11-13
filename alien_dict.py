def alienOrder(words):
    from collections import defaultdict

    graph = defaultdict(list)
    all_chars = set(''.join(words))

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
        for j in range(min_len):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                break

    visited = {}  
    result = []

    def dfs(node):
        if node in visited:
            return visited[node] == 2
        visited[node] = 1  
        for nei in graph[node]:
            if not dfs(nei):
                return False
        visited[node] = 2  
        result.append(node)
        return True

    for char in all_chars:
        if char not in visited:
            if not dfs(char):
                return ""

    result.reverse()
    return ''.join(result)
