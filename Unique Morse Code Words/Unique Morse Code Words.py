class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result = set([])
        
        for i in words:
            tempStr = ''
            for j in i:
                tempStr += code[ord(j) - 97]
            result.add(tempStr)
           
        return len(result)