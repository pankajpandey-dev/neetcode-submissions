class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        cnt = 1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                cnt += 1
            else:
                res.append((cnt, nums[i]))
                cnt = 1
        
        res.append((cnt, nums[-1]))
        res.sort(reverse= True)
        ans = []
        for i in range(k):
            ans.append(res[i][1])

        return ans