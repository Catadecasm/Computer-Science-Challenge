"""The time complexity of the code is O(mn), where m is the number of rows in the grid and n is the number of columns in the grid.
 This is because the DepthFirstSearch() function is called for each cell in the grid, and each call to the function takes linear time.
"""

"""The space complexity of the code is O(mn), where m is the number of rows in the grid and n is the number of columns in the grid.
 This is because the DepthFirstSearch() function uses a visited array to keep track of which cells have already been visited. The size of the visited array is m * n, so the space complexity is O(mn).
"""

#the time and space complexity of the code is O(mn^2) and O(mn), respectively


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        gridPositions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        MaximumGold = [0]  

        def DepthFirstSearch(i, j, totalGold):
            count = grid[i][j]
            totalGold += count
            grid[i][j] = 0
            adresses = 0

            for n in gridPositions:
                row = i + n[0]
                columns = j+ n[1]
                if 0 <= row < len(grid) and 0 <= columns < len(grid[0]):
                    if grid[row][columns] == 0:
                        continue
                    adresses+= 1
                    DepthFirstSearch(row, columns, totalGold)

            if adresses == 0: 
                MaximumGold[0] = max(MaximumGold[0], totalGold)

            totalGold -= count
            grid[i][j] = count

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    DepthFirstSearch(i, j, 0)

        return MaximumGold[0]
		
		
	
		