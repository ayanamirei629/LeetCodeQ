class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        done = False
        paragraph = paragraph.replace('\n', ' ')
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.strip()
        text= paragraph.split(" ")
        times = []
        words =[]
        for pos in range(len(text)):
            tempS = text[pos]
            if len(tempS) > 0:
                tempS = checkStr(tempS,0)
                tempS = checkStr(tempS,len(tempS)-1)
                if tempS not in words:
                    words.append(tempS)
                    times.append(1)
                else:
                    tempP = words.index(tempS)
                    times[tempP] += 1
        while done == False:
            temp_max = max(times)
            temp_pos = times.index(temp_max)
            if words[temp_pos] in banned:
                words.pop(temp_pos)
                times.pop(temp_pos)
            else:
                return words[temp_pos]

def checkStr(word,pos):
    length = len(word)
    if checkASC(ord(word[pos])) == True:
        return word.lower()
    else:
        result = word[0:pos] + word[pos+1:len(word)]
        return result.lower()
    
def checkASC(number):
    if number >= 97 and number <=122:
        return True
    elif number >= 65 and number <= 90:
        return True
    else:
        return False