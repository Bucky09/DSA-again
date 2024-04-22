class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusOne(s: str, j: int) -> str:
            ch = list(s)
            if ch[j] == '9':
                ch[j] = '0'
            else:
                ch[j] = str(int(ch[j]) + 1)
            return ''.join(ch)
        def minusOne(s: str, j: int) -> str:
            ch = list(s)
            if ch[j] == '0':
                ch[j] = '9'
            else:
                ch[j] = str(int(ch[j]) - 1)
            return ''.join(ch)
        deads = set(deadends)
        q1, q2 = set(), set()
        visited = set()
        step = 0
        q1.add("0000")
        q2.add(target)        
        while q1 and q2:
            temp = set()
            for cur in q1:
                if cur in deads:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        temp.add(up)
                    down = minusOne(cur, j)
                    if down not in visited:
                        temp.add(down)
            step += 1
            q1, q2 = q2, temp
        return -1
