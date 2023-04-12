# [문제]
# 소수란 1과 자기 자신으로만 나누어떨어지는 수를 말한다. 예를 들면 1, 2, 3, 5, 17, 101, 10007 등이 소수이다. 이 문제에서는 편의상 1도 소수로 하자.
# 알파벳 대소문자로 이루어진 영어 단어가 하나 있을 때, a를 1로, b를 2로, …, z를 26으로, A를 27로, …, Z를 52로 하여 그 합을 구한다. 예를 들어 cyworld는 합을 구하면 100이 되고, abcd는 10이 된다.
# 이와 같이 구한 수가 소수인 경우, 그 단어를 소수 단어라고 한다. 단어가 주어졌을 때, 그 단어가 소수 단어인지 판별하는 프로그램을 작성하시오.

word = list(input())
sum = 0
for i in range(len(word)):
  if(word[i].isupper() == True):
    sum += (ord(word[i]) - 65 + 27)
  else:
    sum += (ord(word[i]) - 97 + 1)

isPrime = True
for i in range(2, int(sum**0.5)+1):
  if(sum % i == 0):
    isPrime = False
    break

if(isPrime == True):
  print("It is a prime word.")
elif(isPrime == False):
  print("It is not a prime word.")