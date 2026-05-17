class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def search(ind,curr,total):
            if total == target:
                res.append(curr[:])
                return
            if total >target:
                return
            for i in range(ind,len(nums)):
                curr.append(nums[i])
                search(i,curr,total+ nums[i])
                curr.pop()
        search(0,[],0)
        return res
