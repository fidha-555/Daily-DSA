class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n
        