# 별 찍기 - 지그재그

def StAr(n):
    for i in range(n):
        print("* " * ((n+1)//2))
        if((n//2) == 0):
            break
        print(" *" * (n//2))

def main():
    StAr(int(input()))

if __name__ == "__main__":
    main()