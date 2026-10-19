class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev]= i - prev
            stack.append(i)
            
               
        return result

            
        


        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        