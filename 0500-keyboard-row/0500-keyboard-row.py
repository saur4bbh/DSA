class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []

        for word in words:
            r1 = r2 = r3 = 0
            for letter in word.lower():
                if letter in row1:
                    r1 = 1
                elif letter in row2:
                    r2 = 1
                else:
                    r3 = 1
            if r1 + r2 + r3 == 1:
                ans.append(word)
        
        return ans
            

