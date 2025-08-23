class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        a =[]

        for j in range(n):
            if a==[] or a[-1][1] < intervals[j][0]:
                a.append(intervals[j])
            else:
                a[-1][1] = max (a[-1][1], intervals[j][1])

        return a