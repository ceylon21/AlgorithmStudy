import sys
n = int(input())

for i in range(n) :
  line = sys.stdin.readline()
  words = line[:-1].split(" ")
  for i in range(len(words)):
    w = words[i]
    if len(w) > 1:
      ww = ''
      for j in range(len(w)-1, -1, -1):
        ww += w[j]
      words[i] = ww
  
  print(' '.join(words))
