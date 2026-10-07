class Solution(object):
    def isPalindrome(self, s):
        p = ""

        s2=''.join(char.lower() for char in s if char.isalnum())
        p= s2[::-1]

        if p == s2:
            return True
        if p != s2:
            return False
        


    


        """
        :type s: str
        :rtype: bool
        """
        