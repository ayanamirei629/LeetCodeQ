class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        pos = length - 1
        done = False
        while done == False and pos >= 0:
            if digits[pos] != 9:
                digits[pos] += 1
                break
            else:
                digits[pos] = 0
                if pos == 0:
                    digits.insert(0,1)
                    break
                else:
                    pos -= 1
        
        return digits
    
a = Solution()

print a.plusOne([9,7,9])
                    