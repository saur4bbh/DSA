class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1

        ans = 0

        while i<j:
            ans = max((j-i) * min(height[j],height[i]),ans)

            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
            
        return ans
