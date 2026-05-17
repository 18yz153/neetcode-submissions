class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)
        while l<r:
            mid = (l+r)//2
            if target<matrix[mid][0]:
                r=mid
            elif matrix[mid][-1]<target:
                l=mid+1
            else:
                l=mid
                break
        if l >= len(matrix):
            return False
        lstl=0
        lstr=len(matrix[0])
        while lstl<lstr:
            mid = (lstl+lstr)//2
            if target<matrix[l][mid]:
                lstr=mid
            elif matrix[l][mid]<target:
                lstl=mid+1
            else:
                lstl=mid
                return True
        return False