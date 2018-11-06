class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jew = []
        stn = []
        for strJ in range(len(J)):
            jew.append(J[strJ])
        for strS in range(len(S)):
            stn.append(S[strS])
        stn.sort()
        done = False
        posS = 0
        length = len(stn)
        for posJ in range(len(jew)):
            posS = 0
            done = False
            while posS < len(stn) and done == False:
                while len(stn) > posS and stn[posS] == jew[posJ]:
                    stn.pop(posS)
                    if len(stn) > posS and stn[posS] != jew[posJ]:
                        done = True
                posS += 1
        return length - len(stn)  
        