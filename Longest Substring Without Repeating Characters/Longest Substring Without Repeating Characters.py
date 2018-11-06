class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tempS = set([])
        length = len(s)
        ans = 0
        for pos in range(length):
            end = pos
            while end < length and s[end] not in tempS  :
                tempS.add(s[end])
                end += 1
            ans = max(ans, end-pos)
            tempS = set([]) 
        return ans