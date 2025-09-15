class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set()
        for i in brokenLetters:
            broken.add(i)
        
        ans = 1

        word = True
        for letter in text:
            if word and letter in broken:
                ans -= 1
                word = False
            if letter == ' ':
                ans += 1
                word = True
        
        return ans
