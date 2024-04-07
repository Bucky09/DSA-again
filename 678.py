class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmax=0
        leftmin=0
        for i in s:
            if i=='(':
                leftmax+=1
                leftmin+=1
            elif i==')':
                leftmax-=1
                leftmin-=1
            else:
                leftmax+=1
                leftmin-=1
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin=0
        return leftmin==0

        
            
        
