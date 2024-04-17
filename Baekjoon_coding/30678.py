# https://www.acmicpc.net/problem/30678

# 입력받은 숫자만큼 별을 반복해라

n=2

star = [[' ',' ','*',' ',' '], [' ',' ','*',' ',' '], ['*','*','*','*','*'],
        [' ','*','*','*',' '], [' ','*',' ','*',' ']]

size = len(star)
blank = [[' ']*size for _ in range(size)]
print(blank)


def repeat_star(cnt, x, y):
    result = []
    re_val = []

    if cnt == 1:
        return star

    if x == size-1 and y == size-1:
        re_val += blank
        result.append(re_val)
        # print(result)
        re_val = []
        return result
        # (repeat_star(cnt - 1, 0, 0))

    if y == size-1:
        n_x, n_y = x+1, 0
    else:
        n_x, n_y = x, y+1

    if star[x][y] == '*':
        re_val.append(star)
    else:
        re_val.append(blank)

    # result.append(re_val)
    return re_val + repeat_star(cnt, n_x, n_y)

re_star = repeat_star(n, 0, 0)
print(len(re_star))
print(re_star)

m = 0
for i in range(size):
    for k in range(m*size, (m+1)*size):
        for j in range(size):
            print(re_star[k][i][j], end='')
    print()

    m += 1