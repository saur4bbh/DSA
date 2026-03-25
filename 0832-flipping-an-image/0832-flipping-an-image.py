class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        def reverseflip(row):
            i = 0
            j = len(row) - 1
            while i < j:
                row[i], row[j] = row[j] ^ 1, row[i] ^ 1
                i += 1
                j -= 1

            if i == j:
                row[i] = row[i] ^ 1
        
        for row in image:
            reverseflip(row)
        
        return image