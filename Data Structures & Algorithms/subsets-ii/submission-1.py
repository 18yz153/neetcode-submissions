class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtracing(idx,curr):
            res.append(curr[:])
            for i in range(idx,len(nums)):
                if i > idx and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                backtracing(i+1,curr)
                curr.pop()
        backtracing(0,[])
        return res