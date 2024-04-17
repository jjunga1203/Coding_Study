# grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
#Output: [[9,9],[8,6]]

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# Output: [[2,2,2],[2,2,2],[2,2,2]]
print(grid)
N = len(grid)
n = N-2

result_arr = [[0] * n for _ in range(n)]

# 3*3 짜리 영역안에서 최대값을 찾아서 n*n 의 최대치를 찾아라
for i in range(N-3+1):
    for j in range(N-3+1):
        result_arr[i][j] = (max(grid[i][j] , grid[i][j+1] , grid[i][j+2],
                  grid[i+1][j] , grid[i+1][j + 1] , grid[i+1][j + 2],
                  grid[i+2][j] , grid[i+2][j + 1] , grid[i+2][j + 2]))
print(result_arr)