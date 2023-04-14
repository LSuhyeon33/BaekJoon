# [문제] : 거꾸로 구구단
# 단의 수 N과 항의 수 K가 주어질 때, 거꾸로 구구단의 가장 큰 값을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. 두 수는 모두 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 주어진 단과 항에서 나올 수 있는 가장 큰 거꾸로 구구단의 값을 출력한다.

def GUGUDAN_Inv(n, k):
    inv = []
    for i in range(1, k+1):
        inv.append(int(str(n*i)[::-1]))
    return max(inv)

def main():
    n, k = map(int, input().split())
    print(GUGUDAN_Inv(n, k))

if __name__ == "__main__":
    main()