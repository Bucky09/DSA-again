def main(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n
    for i in range(1, n):
        ans[i] = ans[i-1] * nums[i-1]
        
    postfix = 1
    for i in range(n-1,-1,-1):
        ans[i] *= postfix
        postfix *= nums[i]
        
    return str(ans).replace(" ", "")

f = open('user.out', 'w')
for i in stdin:
    nums = list(map(int,i.rstrip()[1:-1].split(r',')))
    print(main(nums), file=f)
    
exit(0)
