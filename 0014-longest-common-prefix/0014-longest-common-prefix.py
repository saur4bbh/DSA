class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = len(strs[0])

        for s in strs[1:]:
            for i in range(idx):
                if i == len(s) or s[i] != strs[0][i]:
                    idx = i
                    break
            if idx == 0:
                return ''
        return strs[0][:idx]
                    