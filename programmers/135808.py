# 사과 최대점수 k
# 상자당 개수 m
# 상자의 가장낮은 사과점수 * m * 상자의 개수 --> 최종 점수
# 이익이 없을시 0

#
def solution(k, m, score):
    answer = 0
    box_cnt = int(len(score)/m)
    score.sort(reverse=True)

    for i in range(0, box_cnt*m, m):
        answer += score[i+m-1] * m * 1

    return answer

k, m = 4,3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

print(solution(k, m, score))

