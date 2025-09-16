class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq = [[] for _ in range(max(count.values())+ 1) ]
        for i,j in count.items():
            freq[j].append(i)
        
        ans = []
        for container in reversed(freq):
            for ele in container:
                ans.append(ele)
                if len(ans) == k:
                    return ans
