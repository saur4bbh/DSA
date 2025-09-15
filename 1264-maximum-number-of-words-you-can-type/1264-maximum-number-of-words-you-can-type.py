class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        ans = 1
        word = True

        for letter in text:
            if letter in broken and word:
                ans -= 1
                word = False
            if letter == ' ':
                ans += 1
                word = True
        
        return ans
