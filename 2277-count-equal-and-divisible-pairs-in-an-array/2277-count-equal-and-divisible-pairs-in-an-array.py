class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        pairs = 0
        
        for i, val in enumerate(nums):
            d[val].append(i)

        for indices in d.values():
            for i in range(len(indices) - 1):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        pairs += 1
        
        return pairs