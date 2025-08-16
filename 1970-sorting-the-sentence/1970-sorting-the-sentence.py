class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        new = [None]*len(l)

        for i in l:
            new[int(i[-1])-1] = i[:-1]
        
        return ' '.join(new)
            
