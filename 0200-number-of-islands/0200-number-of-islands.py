class Solution(object):
    def numIslands(self, grid):
        if len(grid)== 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >=rows or c < 0 or c >= cols or grid[r][c]== "0":
                return
            
            grid[r][c]= "0"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    count += 1
                    dfs(r,c)
        
        return count

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        