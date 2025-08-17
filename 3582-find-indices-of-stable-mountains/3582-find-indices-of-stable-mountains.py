class Solution:
    def stableMountains(self, height: List[int], th: int) -> List[int]:
        return [i for i in range(1,len(height)) if height[i-1]>th]


