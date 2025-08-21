class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        d = {0:1}
        summ = 0
        for val in nums:
            summ += val
            if summ-k in d:
                count += d[summ - k]
            d[summ] = d.get(summ,0) + 1
        
        return count