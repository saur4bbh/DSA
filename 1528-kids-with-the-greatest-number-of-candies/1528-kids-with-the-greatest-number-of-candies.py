class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        big = max(candies) - extraCandies

        for i in range(len(candies)):
            if candies[i] >= big:
                candies[i] = True
            else: 
                candies[i] = False
        
        return candies