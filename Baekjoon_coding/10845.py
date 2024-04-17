# https://www.acmicpc.net/problem/10845
import sys
from collections import deque
sys.stdin = open("10845.md", "r")

T = int(input())

deq = deque()
re_val = ''
re_err = '-1\n'

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    in_val = input().split()

    # push 3
    if in_val[0] == 'push':
        deq.append(in_val[1])
    # 맨 왼쪽 1개 pop
    elif in_val[0] == 'pop':
        if deq:
            re_val += str(deq.popleft()) + '\n'
        else:
            re_val += re_err
    # 맨 앞의 값 출력
    elif in_val[0] == 'front':
        if deq:
            re_val += str(deq[0]) + '\n'
        else:
            re_val += re_err
    # 맨 뒤의 값 출력
    elif in_val[0] == 'back':
        if deq:
            re_val += str(deq[len(deq)-1]) + '\n'
        else:
            re_val += re_err
    # deq 사이즈
    elif in_val[0] == 'size':
        re_val += str(len(deq)) + '\n'
    # 비었는가
    elif in_val[0] == 'empty':
        if deq:
            re_val += '0\n'
        else:
            re_val += '1\n'

print(re_val)