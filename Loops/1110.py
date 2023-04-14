# 더하기 사이클

def Add(num):
    newlist = []
    add = int(num[0]) + int(num[1])
    newlist.append(num[1])
    newlist.append(str(add%10))
    new = int(newlist[0])*10 + int(newlist[1])
    return new

def numList(n):
    numlist = []
    if(n < 10):
        numlist.append('0')
        numlist.append(str(n))
    else:
        numlist = list(str(n))

    return numlist

def Compare(first, new):
    if(first == new):
        return True
    else:
        return False

def main():
    cycle = 0
    check = False
    num = int(input())
    new = Add(numList(num))
    while(check == False):
        check = Compare(num, new)
        new = Add(numList(new))
        cycle += 1

    print(cycle)

if __name__ == "__main__":
    main()