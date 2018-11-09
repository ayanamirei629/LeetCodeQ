# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        solution = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if not solution or interval.start > solution[-1].end:
                solution.append(interval)
            elif interval.end <= solution[-1].end:
                continue
            else: # interval.start <= solution[-1].end and interval.end > =solution[-1].end
                solution[-1].end = interval.end
        return solution
    
    
    
    
    
    
    
a = Solution()
interval7 = [Interval(2,3),Interval(2,2),Interval(3,3),Interval(1,3),Interval(5,7),Interval(2,2),Interval(4,6)]
result =  a.merge(interval7)
for k in range(len(result)):
    print result[k].start
    print result[k].end
    print '---'