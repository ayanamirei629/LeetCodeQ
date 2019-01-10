class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split()
        output = ''
        for word in words:
            output += word[::-1] + ' '
        
        return output.rstrip()
            
        