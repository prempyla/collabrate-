def all_partitions(s):
    results = []
    def backtrack(start, path):
        if start == len(s):
            results.append(path[:])
            return
        for end in range(start+1, len(s)+1):
            path.append(s[start:end])
            backtrack(end, path)
            path.pop()
    backtrack(0, [])
    return results
