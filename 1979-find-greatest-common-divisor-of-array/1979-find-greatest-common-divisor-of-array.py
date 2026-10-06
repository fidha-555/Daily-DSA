class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a= min(nums)
        b= max(nums)
        for i in range(min(a,b),0,-1):
            if a % i == 0 and b % i == 0:
                return i


        