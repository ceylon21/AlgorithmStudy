import sys

deque = []
cnt = int(input())

for i in range(cnt):
  line = sys.stdin.readline()[:-1]
  element = line.split(' ')

  if element[0] == 'push_front':
    deque.insert(0, element[1])
  if element[0] == 'push_back':
    deque.append(element[1])
  elif element[0] == 'pop_front':
    if (len(deque) == 0): print(-1)
    else:
      print(deque[0])
      deque = deque[1:]
  elif element[0] == 'pop_back':
    if (len(deque) == 0): print(-1)
    else:
      print(deque[-1])
      deque.pop()
    
  elif element[0] == 'size':
    print(len(deque))
  elif element[0] == 'empty':
    if (len(deque) == 0): print(1)
    else: print(0)
  elif element[0] == 'front':
    if (len(deque) == 0): print(-1)
    else: print(deque[0])
  elif element[0] == 'back':
    if (len(deque) == 0): print(-1)
    else: print(deque[-1])
  
