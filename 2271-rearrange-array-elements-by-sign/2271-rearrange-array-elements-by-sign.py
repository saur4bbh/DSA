class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        x,y = 0,1
        ans = [None]*len(nums)
        for i in nums:
            if i>0:
                ans[x] = i
                x += 2
            else:
                ans[y] = i
                y += 2
        return ans

