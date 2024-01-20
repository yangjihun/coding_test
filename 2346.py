from collections import deque
N = int(input())
bloon = deque(range(1,N+1))
key = deque(map(int,input().split()))
for _ in range(len(key)):
  print(bloon.popleft(), end=' ')
  if key[0]>0:
    bloon.rotate(key[0]-1)
    key.rotate(key.popleft()-1)
  else:
    bloon.rotate(key[0])
    key.rotate(key.popleft())