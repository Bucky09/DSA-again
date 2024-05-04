class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people.reverse()
        ans, l, r = 0, 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
            ans += 1
        return ans
