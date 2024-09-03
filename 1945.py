class Solution(object):
    def getLucky(self, s, k):
        num=''
        for i in range(len(s)):
            num+=str(ord(s[i])-ord('a')+1)
        
        for i in range(k):
            count=0
            for j in range(len(num)):
                count+=int(num[j]) 
            num=str(count)    
        return int(num)
        
