def solution(s, skip, index):
    answer = ''
    a_list = 'abcdefghijklmnopqrstuvwxyz'

    # skip 문자 제외
    for i in range(len(skip)):
        a_list = a_list.replace(skip[i], '')
    # print(a_list)
    answer = list(s)
    for i, val in enumerate(s):
        # 알파벳 리스트에서 위치 찾기
        find_index = a_list.find(val)
        # index 만큼 이동하여 문자 찾기 (맨 뒤에서 다시 앞으로 돌아가서 찾기)
        final_index = (find_index + index) % len(a_list)
        # print(final_index, a_list[final_index])
        answer[i] = a_list[final_index]
        # print(answer)
    return ''.join(answer)


s, skip, index = "bcdefghijklmnopqrstuvwxyz", "a", 1    #	result	"cdefghijklmnopqrstuvwxyzb"

print(solution(s, skip, index))
