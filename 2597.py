class Solution:
    def beautifulSubsets(self, nums: List[int], difference: int) -> int:
        tot_count = 1
        freq_map = defaultdict(dict)

        # Calculate frequencies based on remainder
        for num in nums:
            remainder = num % difference
            freq_map[remainder][num] = freq_map[remainder].get(num, 0) + 1

        # Iterate through each remainder group
        for fr in freq_map.values():
            n = len(fr)
            curr_count = 1
            next1 = 1
            next2 = 0
            subsets = sorted(fr.items())

            # Calculate counts for each subset starting from the second last
            for i in range(n - 1, -1, -1):
                # Count of subsets skipping the current subset
                skip = next1

                # Count of subsets including the current subset
                take = 2 ** subsets[i][1] - 1

                # If next number has a 'difference', calculate subsets; otherwise, move to next
                if i + 1 < n and subsets[i + 1][0] - subsets[i][0] == difference:
                    take *= next2
                else:
                    take *= next1
                
                # Store the current total count for the current subset
                curr_count = skip + take  
                next2, next1 = next1, curr_count

            tot_count *= curr_count

        return tot_count - 1
