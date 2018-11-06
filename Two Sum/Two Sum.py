class Solution(object):
    def twoSum(self, nums, target):
        mock_nums = list(nums)
        mock_nums.sort()
        for pos1 in range(len(nums)-1):
            if target - mock_nums[pos1] <= mock_nums[len(nums)-1] and target - mock_nums[pos1] >= mock_nums[pos1 + 1]:
                min = pos1 + 1
                max = len(mock_nums)-1
                temp_target = target - mock_nums[pos1]
                if min == max and mock_nums[max] == temp_target:
                    if mock_nums[pos1] == mock_nums[max]:
                        return [nums.index(mock_nums[pos1]), nums.index(mock_nums[max],pos1+1)]
                    else:
                        return [nums.index(mock_nums[pos1]), nums.index(mock_nums[max])]
                while min != max:
                    if mock_nums[(min + max)/2] > temp_target:
                        if min == (min+max)/2:
                            max = min
                        else:
                          max = (min+max)/2  
                    elif mock_nums[(min + max)/2] < temp_target:
                        if mock_nums[max] == temp_target:
                            if mock_nums[pos1] == mock_nums[max]:
                                return [nums.index(mock_nums[pos1]), nums.index(mock_nums[max],pos1+1)]
                            else:
                                return [nums.index(mock_nums[pos1]), nums.index(mock_nums[max])]
                        elif min == (min+max)/2 :
                            min = max
                        else:
                            min = (min+max)/2
                    else:
                        if mock_nums[pos1] == mock_nums[min]:
                            return [nums.index(mock_nums[pos1]), nums.index(mock_nums[(min+max)/2],pos1+1)]
                        else:
                            return [nums.index(mock_nums[pos1]), nums.index(mock_nums[(min+max)/2])]