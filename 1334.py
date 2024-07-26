class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = {i:dict() for i in range(n)}
        for u, v, d in edges:
            if d <= distanceThreshold:
                adj[u][v] = d
                adj[v][u] = d
        
        cities = [0] * n
        for i in range(n):
            count = -1

            distance = [float('inf')] * n
            distance[i] = 0
            visited = [False] * n

            pq = [(0, i)]
            heapify(pq)

            while pq:
                d, node = heappop(pq)
                if d > distanceThreshold:
                    break
                if visited[node]:
                    continue
                visited[node] = True
                count += 1
                for v in adj[node]:
                    if not visited[v] and d + adj[node][v] < distance[v]:
                        distance[v] = d + adj[node][v]
                        heappush(pq, (distance[v], v))
            cities[i] = count

        max_node = 0
        min_distnace = cities[0]
        for i in range(n):
            if cities[i] <= min_distnace:
                max_node = i
                min_distnace = cities[i]
        return max_node
