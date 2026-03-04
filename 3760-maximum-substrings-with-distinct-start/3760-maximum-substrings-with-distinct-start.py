class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = set()
        for character in s:
            seen.add(character)

        return len(seen)