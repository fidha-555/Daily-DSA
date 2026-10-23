class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] = count[num]+1
            else:
                count[num] =1
        max_num =0
        max_count =0
        for num in count:
            if count[num]> max_count:
                max_count =count[num]
                max_num = num
        return max_num 
         
        