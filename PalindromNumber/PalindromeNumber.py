class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_val = x
        if x >= 0:
            answer = ""
            while temp_val >= 10:
                answer += str(temp_val%10)
                temp_val /= 10
            answer += str(temp_val)
            if int(answer) == x:
                return True
        return False