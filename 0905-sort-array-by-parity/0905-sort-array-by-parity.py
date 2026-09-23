class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        evens = []
        odds = []
        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds
