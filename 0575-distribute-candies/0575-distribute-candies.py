class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        half = len(candyType)//2
        n_type = len(set(candyType))
        if n_type < half:
            return n_type
        else:
            return half
            



