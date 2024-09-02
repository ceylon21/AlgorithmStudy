import sys
n = int(input())

for i in range(n) :
  stack = []
  isPerfect = True
  line = sys.stdin.readline()
  for w in line[:-1] : 
    if w == '(' : stack.append(w)
    elif w == ')' :
      if stack : stack.pop()
      else : 
        isPerfect = False
        break

  if not stack and isPerfect : print("YES")
  else : print("NO")