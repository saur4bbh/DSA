class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            present = True
            for i,w in enumerate(pref):
                if i >= len(word) or word[i] != w:
                    present = False
                    break
            if present:
                ans += 1
        return ans