class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        l=intervals[0][0]
        r=intervals[0][1]
        res = []
        for i in range(1,len(intervals)):
            inter = intervals[i]
            if inter[0]>r:
                res.append([l,r])
                l = inter[0]
                r=inter[1]
            else:
                r = max(r,inter[1])
        res.append([l,r])
        return res      