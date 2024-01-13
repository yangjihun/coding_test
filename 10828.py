import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
  m = sys.stdin.readline().split()
  if m[0]=='pop':
    (print(stack.pop())) if len(stack)!=0 else print(-1)
  elif m[0]=='size':
    print(len(stack))
  elif m[0]=='empty':
    print(1 if len(stack)==0 else 0)
  elif m[0]=='top':
    print(stack[-1]) if len(stack)!=0 else print(-1)
  elif m[0]=='push':
    stack.append(m[1])