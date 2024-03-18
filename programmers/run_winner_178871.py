players, callings = ["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"] # ["mumu", "kai", "mine", "soe", "poe"]

flag = False
j = 0
while True:

    caller = callings[j]
    if j != len(callings)-1 and callings[j] == callings[j+1]:
        # 연속해서 두번 불리우는지 체크
        flag = True
        j += 1

    for idx, val in enumerate(players):
        if val == caller:
            # 연속적으로 불리었는가
            if flag == True:
                players[idx - 1], players[idx] = players[idx], players[idx - 1]
                players[idx - 2], players[idx-1] = players[idx-1], players[idx - 2]
                flag = False

            elif idx != 0:
                players[idx-1], players[idx] = players[idx], players[idx-1]
            break
    j += 1

    if j == len(callings):
        break

print(players)