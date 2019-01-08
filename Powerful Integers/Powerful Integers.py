import math
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        
        bag = set([])
        key1 = []
        key2 = []
        time = 0
        
        while math.pow(x, time) <= bound:
            if x == 1:
                key1.append(1)
                break
            key1.append(int(math.pow(x, time)))
            time += 1
        
        time = 0
        while math.pow(y, time) <= bound:
            if y == 1:
                key2.append(1)
                break
            key2.append(int(math.pow(y, time)))
            time += 1
        
        for j in set(key1):
            for i in set(key2):
                if i + j <= bound:
                    bag.add(i+j)
        

        return list(bag)