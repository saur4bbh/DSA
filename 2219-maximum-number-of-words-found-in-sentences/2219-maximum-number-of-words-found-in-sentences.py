class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word = 0
        for i in sentences:
            c = i.count(' ')+1
            if c > word: word = c
        return word