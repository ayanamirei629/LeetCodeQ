class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brS = []
        
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                brS.append(s[i])

            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(brS) <= 0 or brS[-1] != reverseBr(s[i]):
                    return False
                else:
                    brS.pop(-1)

        if len(brS) != 0:
            return False
        return True

def reverseBr(br):
    if br == "]":
        return "["
    if br == ")":
        return '('
    if br == "}":
        return "{"
    
a = Solution()
print a.isValid("(")