class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        numL = []
        timeL = []
        timeCollection = []
        timeNum = time[0:2] + time[3:]
        for i in range(len(timeNum)):
            numL.append(int(timeNum[i]))
        
        numL.sort()
        
        for i in range(len(numL)):
            for j in range(len(numL)):
                if getNum([numL[i],numL[j]]) < 60 and [numL[i],numL[j]] not in timeCollection :
                    timeCollection.append([numL[i],numL[j]])
        
        for min in range(len(timeCollection)):
            temp_min = timeCollection[min]
            if checkMinValid(temp_min) == True:
                if(getNum(temp_min) - getNum([int(timeNum[2]),int(timeNum[3])])) > 0:
                    return  time[0:2] + ':' + str(temp_min[0]) + str(temp_min[1])
        
        print timeCollection.index([int(time[0]),int(time[1])])
        if timeCollection.index([int(time[0]),int(time[1])]) + 1 < len(timeCollection):
            if checkHourValid(timeCollection[timeCollection.index([int(time[0]),int(time[1])]) + 1]) == False:
                return str(timeCollection[0][0]) + str(timeCollection[0][1]) + ":" + str(timeCollection[0][0]) + str(timeCollection[0][1])
            else:
                temp_hour = timeCollection[timeCollection.index([int(time[0]),int(time[1])]) + 1]
                return str(temp_hour[0]) + str(temp_hour[1]) + ":" + str(timeCollection[0][0]) + str(timeCollection[0][1])
        
        else:
            return str(timeCollection[0][0]) + str(timeCollection[0][1]) + ":" + str(timeCollection[0][0]) + str(timeCollection[0][1])
        
def getNum(numList):
    return numList[0] *10 + numList[1]
        
def checkHourValid(timeL):
    if timeL[0]*10 + timeL[1] < 24:
        return True
    return False

def checkMinValid(timeL):
    if timeL[0] * 10 + timeL[1] <60:
        return True
    return False


a = Solution()
time1 = "19:34"
time2 = "23:59"
time3 = "21:22"
print a.nextClosestTime(time3)