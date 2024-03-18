import sys

sys.stdin = open("11660.md", "r")

str = input().split(' ')
N = int(str[0])
k = int(str[1])
tmp_arr = []
arr = []
sum_rows = []
sum_cols = []

# 입력 matrix
for _ in range(0, N):
    tmp = [int(x) for x in input().split(' ')]
    sum_rows.append(sum(tmp))
    arr.append(tmp)

print(sum_rows)

# 구해야 할 범위 test_case
test_cases = []
for _ in range(0, k):
    test_cases.append([int(x) for x in input().split(' ')])

for test_case in test_cases:
    sum = 0
    x1, y1 = test_case[0], test_case[1]
    x2, y2 = test_case[2], test_case[3]

    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            sum += arr[i][j]

    print(f'sum={sum}')
