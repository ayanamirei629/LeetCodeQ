class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''if (len(nums1) + len(nums2)) % 2 == 0:'''
        sumList = []
        num1_pos = 0
        num2_pos = 0
        length = (len(nums1) + len(nums2)) / 2 + 1
        #check if nums1 is empty
        if len(nums1) == 0:
            if len(nums2) == 0:
                return
            else:
                if len(nums2) % 2 == 0:
                    return  (nums2[length - 1] + nums2[length-2]) /float(2)
                else:
                    return   nums2[length-1]
        #check if nums2 is empty
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return  (nums1[length - 1] + nums1[length-2]) /float(2)
            else:
                return   nums1[length-1]
        #loop starts
        while len(sumList) < length:
            while nums1[num1_pos] > nums2[num2_pos]:
                if len(sumList) >= length:
                    break
                sumList.append(nums2[num2_pos])
                num2_pos += 1
                if num2_pos >= len(nums2):
                    for pos in range(len(sumList),length):
                        sumList.append(nums1[num1_pos])
                        num1_pos += 1
                    break
            if num1_pos < len(nums1):
                sumList.append(nums1[num1_pos])
            num1_pos += 1
            if num1_pos >= len(nums1):
                for pos in range(len(sumList),length):
                    sumList.append(nums2[num2_pos])
                    num2_pos += 1
                break
        if (len(nums1) + len(nums2)) % 2 == 0:
            return  (sumList[length - 1] + sumList[length-2]) / float(2)
        else:
            return   sumList[length-1]