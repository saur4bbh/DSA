class Solution:
    def sumOfMultiples(self, n: int) -> int:
        x = (n//7) * ((n//7) + 1) // 2
        y = (n//5) * ((n//5) + 1) // 2
        z = (n//3) * ((n//3) + 1) // 2

        xy = (n//35) * ((n//35) + 1) // 2
        yz = (n//15) * ((n//15) + 1) // 2
        xz = (n//21) * ((n//21) + 1) // 2

        xyz = (n//105) * ((n//105) + 1) // 2

        # inclusion - exclusion principle
        val = 7*x + 5*y + 3*z - 35*xy - 15*yz - 21*xz + 105*xyz
        
        return val
