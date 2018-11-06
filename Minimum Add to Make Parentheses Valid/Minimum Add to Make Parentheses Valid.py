class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        ans1 = 0
        ans2 = 0
        for pos in range(len(S)):
            if S[pos] == "(":
                ans1 += 1
            else:
                if ans1 > 0:
                    ans1 -= 1
                else:
                    ans2 += 1
        return ans1 + ans2