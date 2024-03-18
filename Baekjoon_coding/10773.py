# (1 ≤ K ≤ 100,000)
# 정수는 0에서 1,000,000
# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
import sys
from collections import deque
sys.stdin = open("10773.md", "r")

T = int(input())

new_arr = []

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tmp = int(input())

    if tmp == 0 and new_arr:
        new_arr.pop()
    else:
        new_arr.append(tmp)

print(sum(new_arr))

