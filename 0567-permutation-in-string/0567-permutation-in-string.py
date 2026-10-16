class Solution(object):
    def checkInclusion(self, s1, s2):
        m = len(s1)
        if m > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for char in s1:
            need[ord(char) - ord("a")] += 1

        for right, char in enumerate(s2):
            window[ord(char) - ord("a")] += 1

            if right >= m:
                outgoing = s2[right - m]
                window[ord(outgoing) - ord("a")] -= 1

            if right >= m - 1 and window == need:
                return True

        return False
            
            
        





        


        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        