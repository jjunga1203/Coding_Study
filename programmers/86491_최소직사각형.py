# 최소직사각형
def solution(sizes):
    answer = 0
    x = 0
    y = 0

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            x = max(x, sizes[i][0])
            y = max(y, sizes[i][1])
        else:
            x = max(x, sizes[i][1])
            y = max(y, sizes[i][0])

    answer = x * y
    return answer

# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]	# 4000
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	#120
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	#133

print(solution(sizes))