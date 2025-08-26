class Solution:
    def toLowerCase(self, s: str) -> str:
        gap = ord('a') - ord('A')
        return ''.join(chr(ord(i) + gap) if 65<=ord(i)<=90 else i for i in s)