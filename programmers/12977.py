# 소수 만들기 (3숫자 이용)
# 조합 이용
from itertools import combinations

# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    answer = 0

    combi = list(combinations(nums, 3))
    print(combi)

    for i in range(len(combi)):
        if is_prime_number(sum(combi[i])):
            answer += 1

    return answer

nums = [1,2,3,4]	#1

print(solution(nums))