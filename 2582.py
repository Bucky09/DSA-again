class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dir = time // (n - 1)
        if dir % 2 == 0:
            return 1 + time % (n - 1)
        else:
            return n - (time % (n - 1))
