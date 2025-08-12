class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        value = points[1][0] - points[0][0]

        for i in range(len(points)-1):
            if points[i+1][0]-points[i][0]>value:
                value = points[i+1][0]-points[i][0]

        return value