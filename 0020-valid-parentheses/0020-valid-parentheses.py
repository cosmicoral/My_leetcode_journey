class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            
        return not stack 
            

            
        """
        :type s: str
        :rtype: bool
        """
        