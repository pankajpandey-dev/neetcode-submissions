class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        print(nums)
        maxi = 0
        if n <= 0:
            count = 0
        else:
            count = 1
            maxi = 1
        
        for i in range(n -1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                maxi = max(maxi, count)
                count = 1
        
        return max(maxi,count)
