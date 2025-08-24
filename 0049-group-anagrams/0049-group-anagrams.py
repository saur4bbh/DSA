class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [None] * len(strs)
        d = {}

        j = 0
        for i,val in enumerate(strs):
            ans[i] = tuple(sorted(val))
            if ans[i] not in d:
                d[ans[i]] = j
                j += 1
            
        res = [[] for _ in range(len(d))]
        for i,val in enumerate(ans):
            res[d[tuple(val)]].append(strs[i])

        return res