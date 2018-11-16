class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        ascList =[]
        new_list = []
        for i in range(123):
            ascList.append([])
            
        for pos in range(len(wordDict)): 
            tempS = ''.join(sorted(set(wordDict[pos]), key=wordDict[pos].index))
            if len(tempS) == 1:
                ascList[ord(tempS)].append(len(wordDict[pos])) 
            else:
                new_list.append(wordDict[pos])
        
        for i in range(97,123):
            if 1 in ascList[i]:
                new_list.append(chr(i))
                continue
            if 3 in ascList[i] and 3 in ascList[i]:
                new_list.append(chr(i)*2)
                new_list.append(chr(i)*3)
                continue
            else:
                for j in range(len(ascList[i])):
                    new_list.append(chr(i)* ascList[i][j])
        
        #print new_list
        
        done  = False
        duplicate = True

        probList = [s]
        end_list = []
        while done == False:
            pos = 0
            tempS = ''
            duplicate = True
            for i in range(len(probList)):
                probS = probList[i]
                if len(probS) == 0:
                    return True
                while duplicate == True:
                    if pos + 1 < len(probS) and probS[pos] == probS[pos + 1]:
                        tempS += probS[pos]
                        pos += 1
                    else:
                        tempS += probS[pos]
                        duplicate = False
                if pos > 0:
                    if checkDup(tempS,ascList,probS) == True:
                        probS = probS[len(tempS):]
                        end_list.append(probS)
                        #print probS
                    else:
                        return False
                    print 'tempS: ' + tempS
                else:
                    for j in range(len(new_list)):
                        length = len(new_list[j])
                        if new_list[j] == probS[:length]:
                            if len(probS) == length:
                                return True
                            end_list.append(probS[length:])
                            #print probS[length:]
            probList = end_list
            if len(probList) == 0:
                return False
            end_list = []

                

def checkDup(tempS,ascList,s):
    length = len(tempS)
    temp_l = ascList[ord(tempS[0])]
    if length in temp_l:
        return True
    elif 1 in temp_l or (2 in temp_l and 3 in temp_l):
        return True
    else:
        for i in range(len(temp_l)):
            if length%temp_l[i] in temp_l or length%temp_l[i] == 0:
                return True
    return False
        
        
a= Solution()
b = "leetcode"
c = ["leet","code"]
b1="aaaaaaa"
c1=["aaaa","aa"]
print a.wordBreak(b1,c1)
