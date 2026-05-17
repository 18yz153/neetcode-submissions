class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 1
        i=0
        while i < maxreach:
            maxreach = max(maxreach,i+nums[i]+1)
            i+=1
            if i == len(nums):
                return True
        return False
