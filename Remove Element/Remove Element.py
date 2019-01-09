class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
        
        for j in range(count):
            nums.remove(val)
            
        print nums
        return len(nums)
        

    
    
a=Solution()
print a.removeElement([0,1,2,2,3,0,4,2]
,2)