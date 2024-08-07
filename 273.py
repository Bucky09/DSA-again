class Solution:
    def __init__(self):
        self.ones = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
        self.tens = ["", "Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
        self.thousands = ["", " Thousand", " Million", " Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        result = ""
        count = 0
        while num:
            res = num % 1000
            num //= 1000
            addon = ""
            if res != 0:
                result = self.helper(res) + self.thousands[count] + result
            count += 1

        return result.lstrip()

    def helper(self, num):
        if num < 20:
            return self.ones[num]
        elif num < 100:
            return self.tens[num//10] + self.ones[num%10]
        else:
            return self.ones[num//100] + " Hundred" + self.helper(num%100)
        
