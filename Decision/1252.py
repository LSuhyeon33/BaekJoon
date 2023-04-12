# [문제]
# 두 개의 이진수를 입력받아 이를 더하는 프로그램을 작성하시오.

binNum_1, binNum_2 = input().split()

decNum_1 = int(binNum_1, 2)
decNum_2 = int(binNum_2, 2)

print(bin(decNum_1 + decNum_2)[2:])