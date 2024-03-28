class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {}
        n = len(nums)

        left = 0
        right = left

        largest = 0

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > k:
                largest = max(largest, right - left)
                while nums[left] != nums[right]:
                    counter[nums[left]] -= 1
                    left += 1
                counter[nums[left]] -= 1
                left += 1

            right += 1
        largest = max(largest, right - left)
        return largest
