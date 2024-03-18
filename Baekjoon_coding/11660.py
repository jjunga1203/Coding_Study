# https://www.acmicpc.net/problem/11660

import sys

sys.stdin = open("11660.md", "r")

str = input().split(' ')
N = int(str[0])
k = int(str[1])

result = ''
sum_arr = [[0] * N for _ in range(N)]

# 입력 matrix
for i in range(N):
    # 한줄씩 읽기 -> 1차원 배열로 받기
    tmp = list(map(int, input().split(' ')))
    # print(tmp)
    for j in range(N):
        for idx in range(j+1):
            sum_arr[i][j] += tmp[idx]

# print(sum_arr)

# 구해야 할 범위 test_case
for m in range(k):
    test_case = list(map(int, input().split(' ')))
    sum = 0
    x1, y1 = test_case[0]-1, test_case[1]-1
    x2, y2 = test_case[2]-1, test_case[3]-1

    for i in range(x1, x2+1):
        if y1 != 0:
            sum += (sum_arr[i][y2] - sum_arr[i][y1-1])
        else:
            sum += (sum_arr[i][y2])

    result += f'{sum}\n'

print(result)