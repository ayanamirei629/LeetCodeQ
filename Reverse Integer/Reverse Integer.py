class Solution(object):
    def reverse(self, x):       
        """
        :type x: int
        :rtype: int
        """
        answer = ""
        if x < 0:
            answer += "-"
            x = -x
        while x >= 10:
            answer += str(x%10)
            x /= 10
        answer += str(x)
        if int(answer) > math.pow(2, 31)-1 or int(answer) < -math.pow(2, 31):
            return 0
        return int(answer)

        
