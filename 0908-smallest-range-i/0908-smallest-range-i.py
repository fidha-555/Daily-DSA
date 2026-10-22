class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        min_val = min_val+k
        max_val = max_val -k
        diff  = max_val - min_val
        if diff <0:
            return 0
        else:
            return diff
        