class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        pack = [0] + [-1] * amount
        
        
        coins.sort()
        coins.reverse()
        
        for coin in coins:
            for i in range(coin, amount + 1):
                if pack[i] > -1 and i + coin <= amount:
                    if pack[i + coin] == -1:
                        pack[i + coin] = pack[i] + 1
                    elif pack[i + coin] > pack[i] + 1:
                        pack[i + coin] = pack[i] + 1
                
                if  pack[i] != -1 and i % coin == 0 and i / coin < pack[i]:
                    pack[i] = i / coin
                    
                if pack[i] == -1 and i % coin == 0:
                    pack[i] = i / coin
                

                 

        return pack[amount]