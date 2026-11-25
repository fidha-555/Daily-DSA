class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s =0
        d = 0
        for i in nums:
            if i > 9:
                d+=i
            else:
                s+=i
        if s == d:
            return False
        else:
            return True
        

        