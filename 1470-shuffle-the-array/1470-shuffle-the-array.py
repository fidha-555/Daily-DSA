class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[:n]
        second = nums[n:]
        result = []
        for i in range(n):
            result += [first[i] , second[i]]
        return result