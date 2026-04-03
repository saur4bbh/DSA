class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = set()
        for i in sentence:
            if i.isalpha():
                x.add(i)
        
        return len(x) == 26