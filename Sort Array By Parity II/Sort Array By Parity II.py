class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        pos_n =[ ]
        odd = []
        even = []
        for pos in range(len(A)):
            if pos%2 != A[pos]%2:
                if pos%2 == 0:
                    odd.append(A[pos])
                else:
                    even.append(A[pos])
                pos_n.append(pos)
                
        for i in range(len(pos_n)):
            if pos_n[i]%2 == 0:
                A[pos_n[i]] = even[0]
                even.pop(0)
            else:
                A[pos_n[i]] = odd[0]
                odd.pop(0)
        return A