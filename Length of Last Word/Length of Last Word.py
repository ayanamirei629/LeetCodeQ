class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        
        for i in range(1,n):
            say = checkCount(say)
        
        return say
            

def checkCount(say):
    iniChar = list(say)[0]
    count = 0
    output = ''
    
    for i in list(say):
        if iniChar == i:
            count += 1
        else:
            output += str(count) + iniChar
            iniChar = i
            count = 1
    output += str(count) + iniChar
    print output
    return output

a = Solution()
print a.countAndSay(10)