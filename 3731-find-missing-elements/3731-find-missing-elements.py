class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = 100
        large = 0
        seen = set()
        for num in nums:
            seen.add(num)
            small = min(num, small)
            large = max(num, large)
        
        ans = []
        for i in range(small,large + 1):
            if i not in seen:
                ans.append(i)

        return ans
