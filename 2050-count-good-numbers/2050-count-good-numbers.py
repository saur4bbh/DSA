class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def pow(x, n, mod):
            if n == 0:
                return 1
            if n%2 == 0:
                return pow((x*x)%mod, n//2, mod)
            else:
                return (x * pow(x, n-1, mod))%mod
        
        mod = 10**9 + 7

        prime = pow(4,n//2,mod)
        even = pow(5,(n+1)//2,mod)
        return (prime * even) % mod
