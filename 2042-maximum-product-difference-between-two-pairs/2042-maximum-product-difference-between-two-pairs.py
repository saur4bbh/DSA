class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s1 = s2 = 10**5
        l1 = l2 = 0
        for i in nums:
            if i>l1:
                l2 = l1
                l1 = i
            elif i>l2: l2 = i
            if i<s1: 
                s2 = s1
                s1 = i
            elif i<s2: s2 = i
        return (l1 * l2) - (s1 * s2)

