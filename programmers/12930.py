def solution(s):
    answer = ''

    # 공백을 기준으로 단어별로 구분하여
    # 짝수번째 - 대문자 , 홀수번째 - 소문자
    in_arr = s.split(' ')

    for i in range(len(in_arr)):
        # in_arr[i] = in_arr[i].replace(' ', '')
        in_arr[i] = list(in_arr[i])
        for j in range(len(in_arr[i])):
            if j % 2 == 0:
                in_arr[i][j] = in_arr[i][j].upper()
            else:
                in_arr[i][j] = in_arr[i][j].lower()

        in_arr[i] = ''.join(in_arr[i])

    answer = ' '.join(in_arr)
    return answer

s = "disappeared aPpEaReD"
# 기댓값 〉 "DiSaPpEaReD ApPeArEd"	# "TrY HeLlO WoRlD"
print(solution(s))