class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        charge = 0
        length = min(len(a),len(b))
        pos = -1
        output = ''
        
        

        for pos in range(-1,-length-1,-1):
            temp_sum = int(a[pos]) + int(b[pos]) + charge
            if temp_sum >1 :
                charge = 1
                output = str(temp_sum - 2) + output
            else:
                charge = 0
                output = str(temp_sum) + output
        
        
        if len(a) > len(b):
            maxL = a
        else:
            maxL = b
        
        difL = len(maxL) - length
        if difL != 0:
            for pos in range(difL - 1,-1,-1):
                temp_sum = int(maxL[pos]) + charge
                if temp_sum > 1:
                    charge = 1
                    output = str(temp_sum - 2) + output
                else:
                    output = maxL[0:pos] + str(temp_sum) + output
                    charge = 0
                    break

        if charge == 1:
            output = "1" + output
        
        return output
    
a=Solution()
print a.addBinary("101111",
"10")