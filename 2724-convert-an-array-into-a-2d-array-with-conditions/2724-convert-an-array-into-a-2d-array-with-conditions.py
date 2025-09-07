class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        track = defaultdict(int)
        for i in nums:
            track[i] += 1
        
        rows = max(track.values())
        ans = [[] for _ in range(rows)]

        for val, freq in track.items():
            for j in range(freq):
                ans[j].append(val)
        
        return ans