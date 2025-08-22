class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = [None]*len(cost)
        k = cost[0]
        for i,val in enumerate(cost):
            if val<k: 
                k = val
            ans[i] = k
        return ans


