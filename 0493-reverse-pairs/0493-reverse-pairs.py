class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def mergesort(nums,low = 0, high = None):
            count = 0
            if high == None:
                high = len(nums)-1
            if low < high:
                mid = (low+high)//2
                count += mergesort(nums,low,mid)
                count += mergesort(nums,mid+1,high)
                count += merge(nums,low,mid,high)

            return count
            
        def merge(nums,low,mid,high):
            temp = []
            left = low
            right = mid+1

            cnt = 0                           #Counting reverse on sorted parts
            j = mid + 1
            for i in range(low,mid+1):
                while j<=high and nums[i]>nums[j]*2:
                    j += 1
                cnt += j - (mid + 1)

            while left<=mid and right<=high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            
            while left<=mid:
                temp.append(nums[left])
                left += 1

            while right<=high:
                temp.append(nums[right])
                right += 1

            for i in range(len(temp)):
                nums[low + i] = temp [i]

            return cnt
        
        return mergesort(nums)