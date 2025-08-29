class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        search = []
        if arr[0] > k:
            return k

        ele = arr[0] - 1

        for i in range(1,len(arr)):
            for j in range(arr[i-1]+1,arr[i]):
                search.append(j)
                if len(search) == k - ele: 
                    return search[-1]
                

        return arr[-1] + k - len(search) - ele