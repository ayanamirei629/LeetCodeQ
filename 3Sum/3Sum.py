class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        answer = []

        for pos in range(len(nums)-2):
            if pos == 0 or nums[pos-1] < nums[pos]:
                left = pos +1
                right = len(nums)-1
                temp = nums[pos] + nums[left] + nums[right]
                while left < right:
                    temp = nums[pos] + nums[left] + nums[right]
                    if temp == 0:
                        answer.append([nums[pos],nums[left],nums[right]])
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif temp > 0:
                        right -= 1

                    else:
                        left += 1

        return answer