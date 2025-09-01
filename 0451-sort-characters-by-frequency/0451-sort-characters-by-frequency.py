class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        bucket = [[] for _ in range(len(s) + 1)]

        for val,i in freq.items():
            bucket[i].append(val)

        ans = []
        for i in range(len(bucket)-1,-1,-1):
            for val in bucket[i]:
                ans.append(val*i)
        
        return ''.join(ans)
