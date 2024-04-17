# https://www.acmicpc.net/problem/11660

import sys

sys.stdin = open("11660.md", "r")
input = sys.stdin.readline

str = input().split('\n')
str = str[0].split(' ')
N = int(str[0])
k = int(str[1])

result = ''
sum_arr = [[0] * N for _ in range(N)]


# 입력 matrix
for i in range(N):
    # 한줄씩 읽기 -> 1차원 배열로 받기
    inputs = input().split('\n')
    tmp = list(map(int, inputs[0].split(' ')))
    sums = 0
    # print(tmp)
    for j in range(N):
        sums += tmp[j]
        sum_arr[i][j] = sums

print(sum_arr)

# 구해야 할 범위 test_case
for m in range(k):
    test_case = list(map(int, input().split(' ')))
    sum = 0
    x1, y1 = test_case[0]-1, test_case[1]-1
    x2, y2 = test_case[2]-1, test_case[3]-1

    # print(x1, y1, x2, y2)
    for i in range(x1, x2+1):
        if y1 != 0:
            sum += (sum_arr[i][y2] - sum_arr[i][y1-1])
        else:
            sum += (sum_arr[i][y2])

    result += f'{sum}\n'

print(result)