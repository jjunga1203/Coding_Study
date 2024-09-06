# 세 수의 합이 0이 되는 경우가 몇가지 인가?
# 조합을 이용
from itertools import combinations


def solution(number):
    answer = 0

    combi = list(combinations(number, 3))
    print(combi)

    for i in range(len(combi)):
        if sum(combi[i]) == 0:
            answer += 1

    return answer

number = [-1, 1, -1, 1]
print(solution(number))