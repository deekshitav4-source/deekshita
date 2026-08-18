class Solution(object):
    def largestInteger(self, nums, k):
        from collections import Counter
        n = len(nums)
        # Identify unique elements across the whole array
        counts = Counter(nums)
        
        if k == 1:
            # If k=1, element must appear only once in total
            candidates = [num for num, freq in counts.items() if freq == 1]
            return max(candidates) if candidates else -1
            
        if k == n:
            # If k=n, the max element satisfies the condition
            return max(nums)
            
        # For 1 < k < n, only boundary elements (0 or n-1) can appear 
        # in exactly one window
        ans = -1
        for val in [nums[0], nums[-1]]:
            if counts[val] == 1:
                ans = max(ans, val)
        return ans
        