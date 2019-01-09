class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        desk = s.split()
        if len(desk) == 0:
            return 0
        return len(desk[-1])
        
        
        
        
        
        
        
a=Solution()
print a.lengthOfLastWord("")
