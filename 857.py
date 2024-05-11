class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        res = float('inf')
        _sum = 0
        hp = []
        
        workers = sorted((w/q, q) for w, q in zip(wage, quality))
        
        for w, q in workers:
            heapq.heappush(hp, -q)
            _sum += q
            if len(hp) > k:
                _sum += heapq.heappop(hp)
            if len(hp) == k:
                res = min(res, _sum * w)
                
        return res
