import sys

stack = []
cnt = int(input())

for i in range(cnt):
  line = sys.stdin.readline()[:-1]
  element = line.split(' ')

  if element[0] == 'push' : 
    stack.append(element[1])
  elif element[0] == 'pop' : 
    if (len(stack) == 0) : print(-1)
    else : 
      print(stack[-1])
      stack.pop()
  elif element[0] == 'top' : 
    if (len(stack) == 0) : print(-1)
    else : print(stack[-1])
  elif element[0] == 'size' : 
    print(len(stack))
  elif element[0] == 'empty' : 
    if (len(stack) == 0) : print(1)
    else : print(0)