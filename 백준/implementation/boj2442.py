import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
  print(" " * (N - i) + "*" * (2 * i - 1)) 
# 별 뒤에 공간이 없다...! 항상 제시되는 출력 긁어보기