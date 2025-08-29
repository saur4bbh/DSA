class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l+r) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        
        return r + k + 1
            
