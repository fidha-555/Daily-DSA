class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        biggest = 0
        for c in candies:
            if c > biggest:
                biggest = c
        
        result = []
        for c in candies:
            if c + extraCandies >= biggest:
                result.append(True)
            else:
                result.append(False)
        return result        