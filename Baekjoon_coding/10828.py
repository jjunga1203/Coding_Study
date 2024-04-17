# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


import sys

sys.stdin = open("10828.md", "r")

T = int(input())
stack = []
result_val = ''

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cmd = input()

    if cmd[:4] == 'push':
        cmd_arr = cmd.split(' ')
        stack.append(cmd_arr[1])
    elif cmd == 'pop':
        if stack:
            result_val += f'{stack.pop()}\n'
        else:
            result_val += f'-1\n'
    elif cmd == 'size':
        result_val += f'{len(stack)}\n'
    elif cmd == 'empty':
        if stack:
            result_val += f'0\n'
        else:
            result_val += f'1\n'
    elif cmd == 'top':
        if stack:
            result_val += f'{stack[-1]}\n'
        else:
            result_val += f'-1\n'
        pass

print(result_val)
