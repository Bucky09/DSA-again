from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if [source, destination] in edges:
            return True
        if source == destination:
            return True
        if n <= 1:
            return True

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = {source}

        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False
        
        return dfs(source)
