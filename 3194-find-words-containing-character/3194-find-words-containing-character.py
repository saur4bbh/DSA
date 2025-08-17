class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a = []
        return [i for i,val in enumerate(words) if x in val]
        