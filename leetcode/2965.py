# 예시 1:
# grid = [[1,3],[2,2]]
#  출력: [2,4]
#  설명: 2번은 반복되고 4번은 누락되어 답은 [2,4]입니다.
# 예 2:
#
grid = [[9,1,7],[8,9,2],[3,4,6]]
#  출력: [9,5]
#  설명: 9번은 반복되고 5번은 누락되어 답이 됩니다. [9,5]입니다.

N = len(grid)
print(grid)
cnt_arr = [0] * (N*N)

for i in range(N):
    for j in range(N):
        idx = grid[i][j] - 1
        cnt_arr[idx] += 1

        if cnt_arr[idx] == 2:
            no_2 = idx + 1

for i in range(len(cnt_arr)):
    if cnt_arr[i] == 0:
        no_zero = i+1
        break

result = [no_2, no_zero]
print(result)


