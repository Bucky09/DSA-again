class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        self.solve(0,candidates,target,[],ans)
        return ans
    def solve(self,ind,arr,t,ds,ans):
        if t==0:
            ans.append(ds.copy())
            return 
        for i in range(ind,len(arr)):
            if arr[i]>t:
                break
            if i>ind and arr[i-1]==arr[i]:
                continue
            ds.append(arr[i])
            self.solve(i+1,arr,t-arr[i],ds,ans)
            ds.pop()
        
