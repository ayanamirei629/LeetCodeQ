class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        
        
        for j in range(len(A) - 1, 1, -1):
            for i in range(j-2, -1, -1):
                length = A[i] + A[i + 1]
                if length > A[j]:
                    return length + A[j]
                
        return 0