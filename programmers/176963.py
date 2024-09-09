def solution(name, yearning, photo):
    answer = []
    dict_list = {}

    for i in range(len(name)):
        dict_list[name[i]] = yearning[i]

    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dict_list:
                sum += dict_list[photo[i][j]]
        answer.append(sum)
    return answer


name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
# 결과 [67, 0, 55]

print(solution(name, yearning, photo))
