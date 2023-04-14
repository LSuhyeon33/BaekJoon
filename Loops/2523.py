# [문제] : 피라미드 별찍기

# [입력]
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# [출력]
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

def sTar(n):
    for i in range(1, n+1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)

def main():
    sTar(int(input()))

if __name__ == "__main__":
    main()