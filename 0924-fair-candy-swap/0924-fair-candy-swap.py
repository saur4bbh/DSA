class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bobsum = sum(bobSizes)
        alicesum = sum(aliceSizes)

        bobSizes.sort()

        def bs(target):
            l, r = 0, len(bobSizes) - 1
            while l <= r:
                mid = (l + r) // 2
                if bobSizes[mid] < target:
                    l = mid + 1
                elif bobSizes[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return None

        for i in aliceSizes:
            target = ((bobsum + i) - (alicesum - i)) // 2
            val = bs(target)
            if val != None:
                return [i, bobSizes[val]]