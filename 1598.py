class Solution:
    def minOperations(self, logs: List[str]) -> int:
        route = 0
        while logs:
            tmp = logs.pop(0)
            if tmp == '../':
                if route > 0:
                    route -= 1
            elif tmp == './':
                route += 0
            else:
                route += 1
        return route
        
