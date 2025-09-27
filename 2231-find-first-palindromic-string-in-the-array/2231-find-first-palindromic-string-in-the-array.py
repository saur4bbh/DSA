class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def check(word):
            for i in range(len(word)):
                if word[i] != word[~i]:
                    return False
            return True

        for w in words:
            if check(w):
                return w
                
        return ""