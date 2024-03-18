# 음수의 갯수
# 행방향 / 열방향 모두 증가하지 않는 (감소하거나 같은 형태)
#
# Example 1:
# Input:
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[3,2],[1,0]]

# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0

# import sys
# sys.stdin = open("1351.md", "r")

# grid = input()

print(grid)
# class Solution:
#     # def countNegatives(self, grid: List[List[int]]) -> int:

M = len(grid)
N = len(grid[0])

total_cnt = 0
for i in range(M):
    for j in range(N):
        if grid[i][j] >= 0:
            continue
        total_cnt += (N-j)
        break

print(total_cnt)



