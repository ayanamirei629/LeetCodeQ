class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        number_list = []
        count_list = []
        
        for i in A:
            if i in number_list:
                temp_pos = number_list.index(i)
                count_list[temp_pos] += 1
            else:
                number_list.append(i)
                count_list.append(0)
                
        return number_list[count_list.index(max(count_list))]