class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i,s in enumerate(word):
            if s == ch:
                return word[i::-1] + word[i+1:]
        return word