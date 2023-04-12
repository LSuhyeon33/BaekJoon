# [문제]
# 8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

octNum = input()
decNum = int(octNum, 8)
print(bin(decNum)[2:])