class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

    
        number =[]
        count = []
        uniNum = []
        for i in s:
            if i in number and count[number.index(i)] == True:
                count[number.index(i)] = False
                uniNum.remove(i)
            elif i not in number:
                number.append(i)
                count.append(True)
                uniNum.append(i)
                
        print uniNum
        if len(uniNum) == 0:
            return -1
        else:
            for i in range(len(s)):
                if s[i] in uniNum:
                    return i
                
a=Solution()
print a.firstUniqChar("aadadaad")