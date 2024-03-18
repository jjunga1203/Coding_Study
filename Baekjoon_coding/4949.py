import sys
sys.stdin = open("4949.md", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    tmp_str = input()
    tmp_arr = []
    flag = False

    if tmp_str == '.':
        break

    for val in tmp_str:
        if val == '(' or val == '[':
            tmp_arr.append(val)
        elif val == ')' and len(tmp_arr)>0:
            pop_val = tmp_arr.pop()
            if pop_val != '(':
                flag = True
                break
        elif val == ']' and len(tmp_arr)>0:
            pop_val = tmp_arr.pop()
            if pop_val != '[':
                flag = True
                break
        elif (val == ')' or val == ']') and len(tmp_arr) == 0:
            flag = True

    # print(tmp_arr)
    if flag or len(tmp_arr)>0:
        print('no')
    else:
        print('yes')


    # print(tmp_str)
