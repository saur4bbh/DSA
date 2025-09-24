class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        #not optimal
        cnt = 0
        for i1 in range(len(arr)):
            num1 = arr[i1]
            for i2 in range(i1+1, len(arr)):
                num2 = arr[i2]
                for i3 in range(i2+1, len(arr)):
                    num3 = arr[i3]
                    if abs(num1 - num2) <= a and abs(num2 - num3) <= b and abs(num1 - num3) <= c:
                        cnt += 1

        return cnt