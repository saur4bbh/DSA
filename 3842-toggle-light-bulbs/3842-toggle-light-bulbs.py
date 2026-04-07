class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        light = [0] * 101
        for b in bulbs:
            if light[b] == 0:
                light[b] = 1
            else:
                light[b] = 0

        ans = [i for i,l in enumerate(light) if l == 1]
        return ans
        
        
