class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        switch = True
        flowers = 0

        for i in range(length):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == length - 1 or flowerbed[i+1] == 0

            if switch and left and right and flowerbed[i] == 0:
                flowers += 1
                switch = False

            elif not switch:
                switch = True

        return flowers >= n