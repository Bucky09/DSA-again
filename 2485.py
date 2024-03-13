class Solution:
    def pivotInteger(self, n: int) -> int:
        flag=0
        x=1
        for x in range(n+1):
            s=0
            a=(x*(x+1))//2
            z=x
            while z!=n+1:
                s=s+z
                z=z+1
            if a==s:
                flag=1
                return x
                break
        if flag==0:
            return -1

      
