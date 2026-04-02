class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i2 = idx2 = 0

        for w1 in word1:
            for a1 in w1:
                if i2 >= len(word2[idx2]):
                    idx2 += 1
                    i2 = 0
                if idx2 < len(word2):
                    if a1 != word2[idx2][i2]:
                        return False
                    i2 += 1
                else:
                    return False
        
        if idx2 == len(word2) - 1 and i2 == len(word2[idx2]):
            return True
        else:
            return False

                
            
                
