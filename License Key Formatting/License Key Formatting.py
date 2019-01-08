class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        S = S.upper().replace('-','')
        
        reminder = len(S) % K
        if reminder != 0:
            result = S[:reminder] +'-'
        else:
            result = S[:reminder]
            
        for i in range(reminder, len(S), K):
            result += S[i : i+K] + '-'
        
        return result[:-1]
        
    
    
a = Solution()
print a.licenseKeyFormatting("2-5g-3-J", 2)