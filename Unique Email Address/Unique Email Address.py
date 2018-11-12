class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set([])
        for i in range(len(emails)):
            real_email = ''
            temp_email = emails[i]
            real_email = checkLocal(temp_email) + temp_email[temp_email.index('@'):]    
            result.add(real_email) 
        return len(result)

def checkLocal(email):
    end = email.index('@')
    localName = email[:end]
    if len(localName) == 0:
        return '' 
    
    finish = False
    pos = 0
    output = ''
    while finish == False:
        if localName[pos] == '+':
            finish = True
            break
        elif localName[pos] != '.':
            output += localName[pos]
        pos += 1
        if pos == len(localName):
            finish = True
    return output  

a = Solution()
emails =  ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print a.numUniqueEmails(emails)

#print checkLocal('m.y+3uih2hi@')
