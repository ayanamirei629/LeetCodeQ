class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        output = ''
        
        for i in str:
            output += LowerLetter(i)    
        
        return output
        
        
        
        
        
        
        
        
        
        
def LowerLetter(inputStr):
    if 65 <= ord(inputStr) <= 90:
        return chr(ord(inputStr) + 32)
    else:
        return inputStr
        
a=Solution()
print a.toLowerCase('ewfeEWFWEfw')