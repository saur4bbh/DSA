class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        switch = True
        flowers = 0

        for i in range(length):
            if switch and (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == (length - 1) or flowerbed[i+1] == 0):
                flowers += 1
                switch = False
            elif not switch:
                switch = True

        return flowers >= n