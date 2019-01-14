class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        lengthList = []
        for i in range(len(points)):
            tempP = points[i]
            lengthList.append(checkLen(tempP))
        
        result = []
        
        for i in range(K):
            temp_val = min(lengthList)
            temp_pos = lengthList.index(temp_val)
            result.append(points[temp_pos])
            points.pop(temp_pos)
            lengthList.pop(temp_pos)
            
        return result
    
def checkLen(point):
    return point[0]*point[0] + point[1]*point[1]



a=Solution()
print a.kClosest( [[3,3],[5,-1],[-2,4]] , 2)