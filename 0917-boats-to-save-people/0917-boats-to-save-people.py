class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = [0]*(limit+1)

        for p in people:
            count[p] += 1
        
        j = 0
        for i in range(len(count)):
            while count[i]>0:
                people[j] = i
                count[i] -= 1
                j += 1
        
        i = 0
        j = len(people)-1
        boats = 0

        while i<=j:
            if people[i] + people[j] <= limit:
                i += 1
            boats += 1
            j -= 1

        return boats
        
