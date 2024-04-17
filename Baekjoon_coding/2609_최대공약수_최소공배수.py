# https://www.acmicpc.net/problem/2609

# 첫째 줄에는 두 개의 자연수가 주어진다.
# 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

import sys

sys.stdin = open("2609.md", "r")
arr = input().split()
num1, num2 = [int(x) for x in arr]

# 최대공약수
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a

# 최소공배수
def lcm(a, b):
    return (a*b)/ gcd(a, b)


print('최대공약수 : ', gcd(num1, num2))
print('최소공배수 : ', int(lcm(num1, num2)))



