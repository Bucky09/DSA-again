class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def mysort(conditions):
            # successor for each value (inverted data structure of condition)
            follow = [ set() for _ in range(k + 1) ]
            need   = [ set() for _ in range(k + 1) ]
            for a, b in conditions:
                follow[a].add(b)
                need  [b].add(a)

            # values without any conditions
            open = [ f for f in range(1, k + 1) if not need[f] ]
            seen = set()
            # append successors (if not already done so)
            while open:
                o = open.pop()
                if o not in seen:
                    yield o
                    seen.add(o)

                    for f in follow[o]:
                        need[f].discard(o)
                        if not need[f]:
                            open.append(f)

        # topological sort
        cols = list(mysort(colConditions))
        rows = list(mysort(rowConditions))

        # failed ?
        if len(cols) < k or len(rows) < k:
            return []

        # assign the n-th value to the n-th row/column
        pos = [ -1 ] * ( k + 1 )
        for x, value in enumerate(cols):
            pos[value] = x
        for y, value in enumerate(rows):
            row = [ 0 ] * k
            row[pos[value]] = value
            yield row
