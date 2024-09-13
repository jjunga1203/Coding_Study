def solution(park, routes):
    move = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0)}
    s_i, s_j = 0, 0

    for i, row in enumerate(park):
        for j, element in enumerate(row):
            if element == 'S':
                s_i, s_j = i, j
                break

    for route in routes:
        direc, dist = route.split(' ')
        dist = int(dist)
        di, dj = move[direc]

        valid = True
        ni, nj = s_i, s_j

        for _ in range(dist):
            ni += di
            nj += dj

            if ni < 0 or ni >= len(park) or nj < 0 or nj >= len(park[0]) or park[ni][nj] == 'X':
                valid = False
                break

        if valid:
            s_i, s_j = ni, nj

    return [s_i, s_j]



# 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
# 주어진 방향으로 이동 중 장애물을 나는지 확인합니다.
# 위 두가지 경우 멈추고 다음 명령에 따른다.

# park, routes = ["SOO","OOO","OOO"], ["E 2","S 2","W 1"] #	[2,1]
park, routes =  ["SOO","OXX","OOO"],	["E 2","S 2","W 1"]	#[0,1]
# park, routes =  ["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]	#[0,0]
# park 의 S : 시작 지점
#         O : 이동 가능한 통로
#         X : 장애물

print(solution(park, routes))