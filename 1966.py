from collections import deque

T = int(input())
for _ in range(T):
  N,M = map(int,input().split())
  li = deque(zip(range(N),map(int,input().split())))
  print(li)
  count = 0
  while 1:
    if li[0][1]==max(li):
      li.popleft()
      if count==M:
        print(count+1)
        break
      else:
        count+=1
    else:
      li.rotate()
