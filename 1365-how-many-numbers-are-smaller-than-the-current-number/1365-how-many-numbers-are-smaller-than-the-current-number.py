class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result =[]
        for i in range(len(nums)):
            count =0
            for j in range (len(nums)):
                if nums[j] < nums[i]:
                    count +=1 
            result.append(count)
        return result
        