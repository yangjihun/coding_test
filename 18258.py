import sys
from collections import deque
N = int(sys.stdin.readline())
que = deque([])
for _ in range(N):
  q = sys.stdin.readline().split()
  if q[0]=='push':
    que.append(q[1])
  elif q[0]=='pop':
    print(-1 if not que else que.popleft())
  elif q[0]=='size':
    print(len(que))
  elif q[0]=='empty':
    print(1 if not que else 0)
  elif q[0]=='front':
    print(-1 if not que else que[0])
  elif q[0]=='back':
    print(-1 if not que else que[-1])