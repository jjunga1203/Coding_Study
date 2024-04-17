import sys

sys.stdin = open("1725.md", "r")

T = int(input())
result_val = ''
arr = []
stack = []
pop_arr = []

a_stack = []
area = -9999

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tmp = int(input())
    arr.append(tmp)


for i in range(T):
    tmp = arr[i]

    if stack:
        top_val = stack[-1]
        # 새로 들어온 값이 stack에  있는 값보다 크다면
        if top_val < tmp:
            stack.append(tmp)
        # 작다면/ 같다면
        elif top_val > tmp:
            area_cal = (len(stack)+1) * tmp
            if area < area_cal:
                area = area_cal

            count = 1
            while stack:
                area_cal = stack.pop() * count
                count += 1
                if area < area_cal:
                    area = area_cal

            stack.append(tmp)
        else:
            stack.append(tmp)

    else:
        stack.append(tmp)

# 여전히 스택에 남아있다면 면적구하기
count = 1
while stack:
    area_cal = stack.pop() * count
    count += 1
    if area < area_cal:
        area = area_cal
        # print('넓이: ', area[-1])

# 배열에 가장 작은값 기준 면적 추가하기
min_val = min(arr) * T
if area < min_val:
    area = min_val

print(area)
# print(f'input: {arr}')
# print(f'min: {min_val}')
# print(f'stack: {stack}')
# print(f'area: {area}')