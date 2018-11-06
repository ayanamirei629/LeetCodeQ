class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product1 = [1]
        length = len(nums)
        temp_val = 1
        for pos in range(length-1):
            temp_val *= nums[pos]
            product1.append(temp_val)


        temp_val = 1
        product2 = [1]
        for pos2 in range(length-1):
            temp_val *= nums[-(pos2+1)]
            product2.append(temp_val)


        ans = []
        for i in range(length):
            ans.append(product2[-i-1]*product1[i])
        return ans 