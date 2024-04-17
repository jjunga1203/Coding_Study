# https://www.acmicpc.net/problem/2168

import sys

sys.stdin = open("2168.md", "r")
arr = input().split()
num1, num2 = [int(x) for x in arr]

if num1 <= num2:
    print(num1 * 2)
else:
    print(num2 * 2)