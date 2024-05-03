class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        reversions1 = version1.split(".")
        reversions2 = version2.split(".")

        for i in range(max(len(reversions1),len(reversions2))):
            rev1 = int(reversions1[i]) if i < len(reversions1) else 0
            rev2 = int(reversions2[i]) if i < len(reversions2) else 0

            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1 
        return 0
