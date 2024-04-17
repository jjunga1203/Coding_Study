import sys

sys.stdin = open("11721.md", "r")

input_str = (sys.stdin.readline().strip())

print(input_str)

for i in range(0, len(input_str)+1, 10):
    print(input_str[i:i+10])
