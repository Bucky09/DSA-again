class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        age = 0
        for detail in details:
            age = detail[11] + detail[12]
            if int(age) > 60:
                count += 1
        return count
