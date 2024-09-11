def solution(s):
    answer = 0
    i = 0

    check = True

    while check:
        key_c = s[i]
        i += 1
        cnt1 = 1
        cnt2 = 0

        while cnt1 != cnt2 and i < len(s):
            if key_c == s[i]:
                cnt1 += 1
            else:
                cnt2 += 1
            i += 1

        # cnt1 == cnt2 여서 while 끝남
        answer += 1

        if len(s) == i:
            check = False

    return answer


# s = "banana"	#3
# s = "abracadabra"	#6
s = "aaabbaccccabba" #3

print(solution(s))