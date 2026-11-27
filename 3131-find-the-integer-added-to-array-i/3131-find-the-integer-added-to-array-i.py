class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        x  =nums1
        y = nums2
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                if x[i] > x[j]:
                    temp = x[i]
                    x[i] =x[j]
                    x[j] =temp
        print (x)
        y.sort()
        print(y)
        return y[0] -x[0]



        