class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {1000:"M",900:"CM",500:"D",400:"CD", 100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX", 5:"V",4:"IV",1:"I"}
        list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        answer = ''
        for standardNum in list:
            result = num / standardNum
            if result != 0:
                for times in range(result):
                    answer += dict[standardNum]
                num %= standardNum
        return answer
