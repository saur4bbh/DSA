class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        word = [None]*len(s)
        for i,val in zip(indices,s):
            word[i] = val
        return ''.join(word)