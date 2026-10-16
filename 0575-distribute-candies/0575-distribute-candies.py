class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n=len(candyType)
        allowed = n // 2
        diff_types = set(candyType) 
        count_types = len(diff_types)
        if count_types < allowed:
            return count_types
        else:
            return allowed



        