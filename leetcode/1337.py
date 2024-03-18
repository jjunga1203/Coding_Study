# 1: 군인 0: 시민
# 0앞에는 항상 1이 있어야 한다.
# 약한 K 개수 만큼 반환

# 동일하다면 i < j 표현
# 1이 작을 수록 약함.
# 1의 갯수가 가장 작은 순서대로 내열


mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3

N = len(mat)
M = len(mat[0])

arr = [[0] * 2 for _ in range(N)]

for i in range(N):
    arr[i][0] = i
    for j in range(M):
        arr[i][1] += mat[i][j]

arr.sort(key=lambda x:x[1])

result = []
for i in range(k):
    result.append(arr[i][0])

print(result)