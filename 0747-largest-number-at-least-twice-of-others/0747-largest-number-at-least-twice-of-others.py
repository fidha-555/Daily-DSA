class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        lar = max(nums)
        ind = nums.index(lar)
        for i in nums:
            if i != lar and i*2 > lar:
             return -1
        return ind
        