class Solution:
    def minimumSum(self, num: int) -> int:
        a=[num%10,(num//10)%10,(num//100)%10,(num//1000)%10]
        a.sort()
        return (a[0]+a[1])*10+a[2]+a[3]