# https://www.acmicpc.net/problem/2571
import sys

sys.stdin = open("2571.md", "r")
input = sys.stdin.readline

heap = []
T = int(input())

sq = []
area = []
len_val = 10

def cal_area(idx):
    re_val = 0

    for i in range(idx):
        cross_x = sq[i+1][0][0] - sq[i][0][0]
        cross_y = sq[i+1][0][1] - sq[i][0][1]
        if (cross_x != 10) and (cross_y != 10):
            area_val = (len_val + cross_x) * (len_val + cross_y)
            # area_val = (cross_x) * (abs(cross_y))
            print(area_val)
        continue

        # print(sq[i+1][0][0] - sq[i][0][0])
        # print(sq[i+1][0][1] - sq[i][0][1])
        # print(sq[i])

    return re_val

for i in range(1, T+1):
    arr = input().split()
    ax, ay = [int(x) for x in arr]

    # 1. 값을 읽어 왼/아 모서리 포인트 잡고
    # 2. 10만큼의 면적을 가진 위/오 모서리 포인트 설정
    sq.append([[ax, ay], [ax+10, ay+10]])



# 시작 지점 기준으로 sorting
sq.sort()
b_area = 100

for i in range(len(sq)):
    # 이전 면적이 있으면 저장해 놓는다.
    if len(area) == 0:
        area.append(b_area)
    else:
        # 겹치는 면적 구하기
        cal_area(i)

# 겹치는 면적 구하기

print(sq)
    # print(num1, num2)