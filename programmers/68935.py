# 1. n 을 3진법으로 변환
# 2. 해당 값을 앞뒤로 뒤집기
# 3. 10진법으로 변환

def get_numsys(n, sys_num):
    # 10진법을 다른 진법으로 변환
    # 결과를 뒤집어서 반환함.

    result = ''
    remain = n
    while remain > 1:
        result += str(remain % sys_num)
        remain = remain // sys_num
        # print(remain, result)

    result += str(remain)
    print(result)
    return result


def solution(n):
    answer = 0
    result = get_numsys(n, 3)
    j = len(result)-1
    # 다시 10진법으로 변환
    for i in range(len(result)):
        answer += int(result[i]) * (3**j)
        j -= 1

    return answer

print(solution(90))