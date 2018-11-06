class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {"I":1, "V":5,"X":10,"L":50, "C":100,"D":500,"M":1000}
        dict2 = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        sum = 0
        pos = 0
        while pos < len(s):
            if  pos + 1 < len(s) and dict2.has_key(s[pos]+s[pos+1]):
                sum += dict2[s[pos]+s[pos+1]]
                pos += 2
            else:
                sum += dict1[s[pos]]
                pos += 1
        return sum
                
            
        