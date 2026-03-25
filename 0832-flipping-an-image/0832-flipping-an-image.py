class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        def reverseflip(row):
            i = 0
            j = len(row) - 1
            while i < j:
                row[i] = 1 - row[i]
                row[j] = 1 - row[j]
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1

            if i == j:
                row[i] = 1 - row[i]
        
        for row in image:
            reverseflip(row)
        
        return image