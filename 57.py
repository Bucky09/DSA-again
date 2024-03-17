class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, n in enumerate(intervals):
            if newInterval[1] < n[0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > n[1]:
                res.append(n)

            else:
                newInterval = [min(newInterval[0], n[0]), max(newInterval[1], n[1])]

        res.append(newInterval)

        return res
