class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        Total = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                Total += cost[i]
        return Total

        