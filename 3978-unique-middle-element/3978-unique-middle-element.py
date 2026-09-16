class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle = nums[len(nums) // 2]
        if nums.count(middle) == 1:
            return True
        else:
            return False