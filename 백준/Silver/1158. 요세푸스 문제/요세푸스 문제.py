N, k = map(int, input().split())
arr = [i for i in range(1, N+1)]
ans = []
idx = k - 1

# 원형 큐
for i in range(N) :
  if idx >= len(arr) :
    idx = idx % len(arr)
    ans.append(str(arr.pop(idx % len(arr))))
  else : 
    ans.append(str(arr.pop(idx)))
  idx += k - 1

print("<" + ", ".join(ans) + ">")