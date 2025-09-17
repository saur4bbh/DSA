class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i,h in enumerate(heights):
            names[i] = [h, names[i]]

        names.sort(reverse = True)

        for i,n in enumerate(names):
            names[i] = names[i][1]
        
        return names