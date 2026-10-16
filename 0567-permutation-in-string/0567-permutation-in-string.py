class Solution(object):
    def checkInclusion(self, s1, s2):
        left = 0
        a = sorted(s1)

        for left in range(len(s2) - len(s1)+1):
            window = s2[left:left+len(s1)]
            if a != sorted(window):
                left +=1
            if a == sorted(window):
                return True
            
        return False 
            
            
        





        


        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        