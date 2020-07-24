'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        result = [None] * len(grid)
        for i in range(len(result)):
            result[i] = [0] * len(grid[i])
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    result[i][j] = grid[i][j]
                elif i == 0:
                    result[i][j] = grid[i][j] + result[i][j-1]
                elif j == 0:
                    result[i][j] = grid[i][j] + result[i-1][j]
                else: 
                    result[i][j] = grid[i][j] + min(result[i][j-1], result[i-1][j])
        
        return result[-1][-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(Solution().minPathSum(grid))
