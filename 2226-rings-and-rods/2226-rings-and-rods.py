class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(list)

        for i in range(1,len(rings),2):
            rods[rings[i]].append(rings[i-1])

        return sum(len(set(x)) == 3 for x in rods.values())