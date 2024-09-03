# s = 'banana'

def solution(s):
    answer = []

    # 0. 영어 소문자만 들어온다.
    #    키-value로 위치를 저장한다.
    # 1. 모든 글자를 순회하며, 키의 밸류가 존재하면 계산하고, 업데이트한다.
    # 2. 밸류가 존재하지 않으면, 해당값을 업데이트하고 -1로 리턴한다.

    alpha_dic = {}
    for idx, val in enumerate(s):
        if val in alpha_dic:
            pre_idx = alpha_dic[val]
            alpha_dic[val] = idx
            answer.append(idx - pre_idx)
        else:
            alpha_dic[val] = idx
            answer.append(-1)

    return answer

print(solution('foobar'))