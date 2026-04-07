class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        peeps = [0] * 100
        for i in logs:
            for t in range(i[0], i[1]):
                peeps[t - 1950] += 1
        
        population = 0
        year = 0
        for i, peep in enumerate(peeps):
            if peep > population:
                population = peep
                year = i + 1950
        
        return year
