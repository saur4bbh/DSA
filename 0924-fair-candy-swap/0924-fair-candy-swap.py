class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bobset = set()
        bobsum = 0
        for j in bobSizes:
            bobset.add(j)
            bobsum += j
        
        alicesum = sum(aliceSizes)

        for i in aliceSizes:
            num = ((bobsum + i) - (alicesum - i)) // 2
            if num in bobset:
                return [i, num]