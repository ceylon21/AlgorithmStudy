import sys

queue = []
cnt = int(input())

for i in range(cnt):
  line = sys.stdin.readline()[:-1]
  element = line.split(' ')

  if element[0] == 'push':
    queue.append(element[1])
  elif element[0] == 'pop':
    if (len(queue) == 0): print(-1)
    else:
      print(queue[0])
      queue = queue[1:]
  elif element[0] == 'size':
    print(len(queue))
  elif element[0] == 'front':
    if (len(queue) == 0): print(-1)
    else: print(queue[0])
  elif element[0] == 'back':
    if (len(queue) == 0): print(-1)
    else: print(queue[-1])
  elif element[0] == 'empty':
    if (len(queue) == 0): print(1)
    else: print(0)
