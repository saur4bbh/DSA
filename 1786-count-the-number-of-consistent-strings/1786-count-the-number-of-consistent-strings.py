class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = set(allowed)
        ans = 0

        for i in words:
            consistent = True
            for j in i:
                if j not in chars:
                    consistent = False
            if consistent:
                ans += 1

        return ans