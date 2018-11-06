class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_val = nums[0]
        sub_val = 0
        length = len(nums)
        for pos in range(length):
            tempV = nums[pos]
            if tempV <= 0:
                sub_val += tempV
                if max_val < tempV:
                    max_val = tempV
            else:
                if sub_val > 0 and sub_val + tempV > max_val:
                    max_val = sub_val + tempV
                    sub_val = tempV + sub_val
                elif sub_val <= 0 and tempV > max_val:
                    max_val = tempV
                    sub_val = tempV
                elif tempV + sub_val < tempV:
                    sub_val = tempV
                else:
                    sub_val += tempV
        return max_val
