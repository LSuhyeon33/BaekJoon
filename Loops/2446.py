# 별 찍기 - 모래시계

def StaR(n):
    for i in range(n, 0, -1):
        print(" " * (n-i), end="")
        print("*" * (i*2-1))
    for i in range(2, n+1):
        print(" " * (n-i), end="")
        print("*" * (i*2-1))

def main():
    StaR(int(input()))

if __name__ == "__main__":
    main()