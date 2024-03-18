mat = [[0,0],[1,1],[0,0]]

N = len(mat)
M = len(mat[0])

arr = [0] * N
idx_min = [0, -9999]

for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            arr[i] += 1

    if idx_min[1] < arr[i]:
        idx_min = [i, arr[i]]
print(idx_min)