class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLen1 = (len(s)-1)/2
        strLen2 = len(s)/2
        if len(s) <= 1:
            return s
        if len(s) == 2:
            if s [0] == s [-1]:
                return s
            return s[0]
        curMax = 0
        cur_info = [0,s[0]]
        answer = ''
        done = False;
        #odd length
        if len(s)%2 == 1:
            #ABA
            left = strLen1-1
            right = strLen1+1 
            mid = strLen1

            tempLen = checkOddLen(s,mid,strLen1)

            if  tempLen == strLen1:
                done = True
                cur_info=[len(s), s]
            elif tempLen > cur_info[0]:
                cur_info = [tempLen,getOddAnswer(s,mid,tempLen)]
            strLen1 -= 1    

            #(s,done,left,right,strLen1,cur_info)
            cur_info = checkABA(s,done,left,right,strLen1,cur_info)

            #AABB
            strLen1 = (len(s)-1)/2
            left = strLen2 - 1
            right = strLen2
            done =  False
            tempLen = checkEvenLen(s,left,strLen1)
            if tempLen == strLen1:
                done = True
                if cur_info[0] < tempLen:
                    cur_info= [tempLen,getEvenAnswer(s,left,tempLen)]
            elif tempLen > cur_info[0]:
                cur_info = [tempLen,getEvenAnswer(s,left,tempLen)]
            tempLen = checkEvenLen(s,right,strLen1)
            if tempLen == strLen1:
                done = True
                if cur_info[0] < tempLen:
                    cur_info= [tempLen,getEvenAnswer(s,right,tempLen)]
            elif tempLen > cur_info[0]:
                cur_info= [tempLen,getEvenAnswer(s,right,tempLen)]
            left -= 1
            right+= 1
            strLen1 -= 1
            #(s,done,left,right,strLen1,cur_info)
            cur_info = checkAB(s,done,left,right,strLen1,cur_info);

        if len(s)%2 == 0:
            #ABA
            done =  False
            left = strLen2-1
            right = strLen2
            cur_info = checkABA(s,done,left,right,strLen1,cur_info)

            done =  False
            mid = strLen2 - 1
            left = strLen2 - 2
            right = strLen2
            tempLen = checkEvenLen(s,mid,strLen2)
            if tempLen == strLen2:
                done = True
                if cur_info[0] < tempLen:
                    cur_info= [tempLen,getEvenAnswer(s,mid,tempLen)]
            elif tempLen > cur_info[0]:
                cur_info = [tempLen,getEvenAnswer(s,mid,tempLen)]


            #do 1 time
            cur_info = checkAB(s,done,left,right,strLen1,cur_info)

        return cur_info[1]

def checkOddLen(s,pos, strLen):
    maxLen = 0
    for curLen in range(1,strLen+1):
        if s[pos - curLen] ==  s [pos + curLen]:
            maxLen += 1
        else:
            break;
    return maxLen 

def checkEvenLen(s,pos, strLen):
    maxLen = 0
    for curLen in range(0,strLen):
        if s[pos - curLen] ==  s [pos + curLen+1]:
            maxLen += 1
        else:
            break;
    return maxLen 

def getOddAnswer(s,pos,strLen):
    return s[pos-strLen: pos+ strLen+1]

def getEvenAnswer(s,pos,strLen):
    return s[pos-strLen+1: pos+ strLen+1]    

def checkABA(s,done,left,right,strLen1,cur_info):
    while done == False and left > 0:
            tempLen = checkOddLen(s,left,strLen1)
            if  tempLen > cur_info[0]:
                cur_info = [tempLen, getOddAnswer(s,left,tempLen)]
                if tempLen == strLen1:
                    done = True
                    break;          
            tempLen = checkOddLen(s,right,strLen1)    
            if  tempLen > cur_info[0]:
                cur_info =[ tempLen,getOddAnswer(s,right,tempLen)]
                if tempLen == strLen1 :
                    done = True
                    break;  
            left -= 1
            right += 1
            strLen1 -= 1
    return cur_info            

def checkAB(s,done,left,right,strLen1,cur_info):
    while done == False and left >= 0:
            tempLen = checkEvenLen(s,left,strLen1)
            if  tempLen > cur_info[0]:
                cur_info= [tempLen,getEvenAnswer(s,left,tempLen)]
                if  tempLen == strLen1:
                    done = True    
                    break;
            tempLen = checkEvenLen(s,right,strLen1)
            if  tempLen > cur_info[0]:
                cur_info= [tempLen,getEvenAnswer(s,right,tempLen)]
                if tempLen == strLen1:
                    done = True    
                    break;
            left -= 1
            right+= 1
            strLen1 -= 1
    return cur_info