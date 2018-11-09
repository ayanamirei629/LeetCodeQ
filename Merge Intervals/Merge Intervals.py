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
        output = []
        equal_list = []
        total_list = []
        if len(intervals) == 0:
            return []
        final_list = set([])
        for pos in range(len(intervals)):
            if intervals[pos].start == intervals[pos].end:
                equal_list.append(intervals[pos].start)
            else:
                for i in range(intervals[pos].start,intervals[pos].end):
                    final_list.add(i)
                    total_list.append(i)
                total_list.append(intervals[pos].end)
        
        total_list = list(set(total_list))
        equal_list = list(set(equal_list))
        for k in range(len(equal_list)):
            if equal_list[k] not in total_list:
                output.append(Interval(equal_list[k],equal_list[k]))
            
        if len(final_list) == 0:
            return output   
        
        min_index = min(final_list)
        max_index = max(final_list)
        temp_start = min_index
        
        isStart = False
        for j in range(min_index, max_index + 1):
            if isStart == False and j not in final_list:
                output.append(Interval(temp_start,j))
                isStart = True
                temp_start = -1
            if isStart == True and j in final_list and temp_start == -1:
                temp_start = j
                isStart = False
            if isStart == False and j == max_index:
                output.append(Interval(temp_start,j+1))
                
        return output

        
        
        
        
        
        
        
a = Solution()
interval1 = [Interval(1,4),Interval(4,5)] 
interval2 = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
interval3 = []
interval4 = [Interval(1,4),Interval(5,6)]
interval5 = [Interval(0,0),Interval(0,0),Interval(3,3),Interval(1,1),Interval(1,1)]
interval6 = [Interval(2,3),Interval(5,5),Interval(2,2),Interval(3,4),Interval(3,4)]
interval7 = [Interval(2,3),Interval(2,2),Interval(3,3),Interval(1,3),Interval(5,7),Interval(2,2),Interval(4,6)]
result =  a.merge(interval7)
for k in range(len(result)):
    print result[k].start
    print result[k].end
    print '---'