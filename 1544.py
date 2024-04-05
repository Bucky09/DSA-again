class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        s = deque(s)
        stk = []
        while s:
            stk.append(s.popleft())
            if len(stk) >= 2 and \
               (stk[-1] != stk[-2] and stk[-1].lower() == stk[-2].lower()):
               stk[:] = stk[:-2]
            
        return ''.join(stk)
