class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)

        for i in range(1,len(rings),2):
            rods[rings[i]].add(rings[i-1])

        return sum(len(x) == 3 for x in rods.values())