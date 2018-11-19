class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        strDict = dict({2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'})
        
        done = False
        pos = 0
        posList = []
        if len(digits) == 0:
            return []
        while done == False:
            if strDict.has_key(int(digits[pos])):
                posList = PosList(posList, strDict[int(digits[pos])])
                pos += 1
            else:
                pos = pos + 1
            if pos >= len(digits):
                break
        return posList
            
        
def PosList(posList, letterStr):
    new_list = []
    for i in range(len(posList)):
        for j in range(len(letterStr)):
            new_list.append(posList[i] + letterStr[j]) 
     
    if len(posList) == 0:
        for i in range(len(letterStr)):
            new_list.append(letterStr[i]) 
    return new_list        
    
    
    
a = Solution()
digit1 = '23'
digit2 = ''