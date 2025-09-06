class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1

        return [i for i,j in seen.items() if j == 2]