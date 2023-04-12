# [문제]
# 중앙 이동 알고리즘

dot = []
dot.append(4)
for i in range(1, 16):
  # dot[i] = (dot[i-1] * 4) - (4 * (2**(i-1)) + 3)
  dot.append((dot[i-1] * 4) - (4 * (2**(i-1)) + 3))

n = int(input())
print(dot[n])