# 주어진 2차원 배열에서
# 각 행별로 최대값을 제거하는 스텝 (한 스텝마다 큰 값을 더한다.)
# 마지막 1개의 열이 될때까지 진행
# 아래 행열의 경우
# (1단계 : 0행 4제거, 1행 3제거 -> 큰값 4)
# (2단계 : 0행 2제거, 1행 3제거 -> 큰값 3)
# (3단계 : 0행 1제거, 1행 1제거 -> 큰값 1)
# 결과 8
grid = [[1,2,4],[3,3,1]]

N = len(grid)
M = len(grid[0])

arr = [0] * N
max_val = [[0] * N]*2

for i in range(N):
    for j in range(M):
        if max_val[i][0] < grid[i][j]:
            max_val[i][0] = grid[i][j]
            max_val[i][1] = j
    print(max_val[i])
