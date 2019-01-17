class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[::-1] == s:
            return True
        else:
            for i in range(len(s)/2):
                if s[i] != s[len(s) - 1 - i]:
                    temp_s = list(s)
                    temp_s.pop(i)
                    if temp_s[::-1] == temp_s:
                        return True
                    temp_s = list(s)
                    temp_s.pop(len(s) - 1 - i)
                    if temp_s[::-1] == temp_s:
                        return True
                    else:
                        return False
        return False
a=Solution()
print a.validPalindrome('accba')