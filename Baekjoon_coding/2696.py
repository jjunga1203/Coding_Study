# 어떤 수열을 읽고, 홀수번째 수를 읽을 때 마다,
# 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.
#
# 예를 들어, 수열이 1, 5, 4, 3, 2 이면,
# 홀수번째 수는 1번째 수, 3번째 수, 5번째 수이고,
# 1번째 수를 읽었을 때 중앙값은 1, 3번째 수를 읽었을 때는 4, 5번째 수를 읽었을 때는 3이다.

import sys
sys.stdin = open("2696.md", "r")
# input = sys.stdin.readline

T = int(input())
print(T)

for i in range(1, T+1):
    M = int(input())
    print(M)
    arr = []

    loop_cnt = M // 10 + 1
    for i in range(loop_cnt):
        if arr:
            arr += list(map(int, input().split()))
        else:
            arr = list(map(int, input().split()))

    print(arr)
