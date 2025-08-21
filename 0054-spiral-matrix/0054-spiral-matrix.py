class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        right = len(matrix[0])-1
        bot = len(matrix)-1

        soln = []

        while left<=right and top<=bot:
            for i in range(left,right+1):
                soln.append(matrix[top][i])
            top += 1
            
            for i in range(top,bot+1):
                soln.append(matrix[i][right])
            right -= 1

            if top<=bot:
                for i in range(right,left-1,-1):
                    soln.append(matrix[bot][i])
                bot -= 1

            if left<=right:
                for i in range(bot,top-1,-1):
                    soln.append(matrix[i][left])
                left += 1

        return soln

