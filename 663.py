class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i,j=0,int(math.sqrt(c))
        while i<=j:
            sum1=i*i+j*j
            if sum1==c:
                return True
            elif sum1>c:
                j-=1
            else:
                i+=1
        return False
