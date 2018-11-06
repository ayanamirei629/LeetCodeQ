class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        rowL = len(grid)
        
        for row in range(rowL):
            colL = len(grid[row])
            for col in range(colL):
                if grid[row][col] == '1':
                    grid[row][col] = 0
                    grid = checkNeighbor(row,col,grid)
                    count += 1
 
        return count

def checkNeighbor(row,col,grid):
    posL = []
    if row >= 1 :
        grid = checkPos(row-1,col,grid)
    if col>= 1:
        grid = checkPos(row,col-1,grid)
    if col < len(grid[row]) - 1:
        grid = checkPos(row,col+1,grid)
    if row < len(grid) - 1:
        grid = checkPos(row+1,col,grid)
    return grid         

def checkPos(row,col,grid):
    if grid[row][col] == '1':
        grid[row][col] = 0
        grid[row][col] = 0
        grid = checkNeighbor(row,col,grid)
    return grid