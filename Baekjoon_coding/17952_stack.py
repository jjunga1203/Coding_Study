# https://www.acmicpc.net/problem/17952

import sys

sys.stdin = open("17952.md", "r")
input = sys.stdin.readline

T = int(input())

stack = []
re_val = 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tmp = input().split('\n')
    tmp = tmp[0]

    if tmp == '0':
        # 이전 과제를 한다
        if stack:
            max_s, cal_time = stack.pop()
            if cal_time == 1:
                re_val += max_s
            else:
                stack.append([max_s, cal_time-1])

        continue

    hw_flag, max_score, during = tmp.split(' ')

    max_score = int(max_score)
    during = int(during)

    # 과제 받자마자 바로 수행함.
    if during == 1:
        re_val += max_score
        continue

    # 0 이면 이전 과제 이어서 한다.
    # 1 이면 새로운 과제를 한다.
    # 새로운 과제가 끝나면 이전 과제를 한다.

    stack.append([max_score, during-1])

print(re_val)

