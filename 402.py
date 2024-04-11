class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        stack=[]
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k-=1
            stack.append(num[i])

        stack=stack[:len(stack)-k ]
        return "".join(stack).lstrip("0") or "0"
        
