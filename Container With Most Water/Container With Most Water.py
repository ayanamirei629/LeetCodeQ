class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_height = height[0]
        max_pos = 0
        pre_pos = 0
        pre_height = height[0]
        max_val = 0
        count = False
        length = len(height)
        for pos in range(1,length):
            tempH = height[pos]
            ratio = ((length - max_pos - 1)*max_height)-( tempH * (length - pos - 1))
            temp_val = getVal(max_pos,max_height,pos,tempH)
            pre_val = getVal(pre_pos,pre_height,pos,tempH)
            if max_height >= tempH:       
                if temp_val > max_val:
                    max_val = temp_val
                if pre_val > max_val:
                    max_val = pre_val
            elif ratio >= 0 and max_height < tempH:
                if temp_val > max_val:
                    max_val = temp_val
                if pre_val >max_val:
                    max_val = pre_val
            else:

                future_valP = pre_height * (length - 1 - pre_pos)
                future_valM = max_height * (length - 1 - max_pos)
                
                if future_valP < future_valM or count == False:
                    pre_height = max_height
                    pre_pos = max_pos
                    count = True
                if temp_val >= max_val:
                    max_val = temp_val
                if pre_val > max_val:
                    max_val = pre_val 
                max_pos = pos
                max_height = tempH
        return max_val;
def getVal(pos,height,tempP,tempH):
    if height > tempH:
        return tempH*(tempP-pos)
    else:
        return height*(tempP-pos)