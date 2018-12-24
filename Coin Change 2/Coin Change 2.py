class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        
        pack = [1] + [0] * amount
        
        coins.sort()  
        pre_amount = 0
        
        for i in coins:
            temp_pack = list(pack)
            
            for j in range(i,amount + 1):         
                pack[j] += pack[j - i]
        
        
        return pack[amount]      
        
        
        
        
a=Solution()
print a.change(100,[99,1])