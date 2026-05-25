class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=  []
        for i in range(0,len(nums)):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r] ==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] ==nums[l-1]:
                        l+=1
                elif nums[i]+nums[l]+nums[r] >0:
                    r-=1
                else:
                    l+=1
        return res