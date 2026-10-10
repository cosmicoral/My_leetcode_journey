class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0 
        right = 0
        result = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            result= max(result,len(seen))

        
        return result
        """
        :type s: str
        :rtype: int
        """
        