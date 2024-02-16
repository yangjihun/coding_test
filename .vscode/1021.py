from collections import deque
N,M = map(int,input().split())
li = deque(range(1,N+1))
A = list(map(int,input().split()))
result = 0
key = 0

while key!=M:
  if li[key]==A[key]:
    li.popleft()
    key+=1
  else:
    if (len(li)//2-li.index(A[key]))>0:
      li.rotate(len(li)//2-li.index(A[key]))
      li.popleft()
      result+=(len(li)//2-li.index(A[key]))
      key+=1
    else:
      li.rotate(-(len(li)//2-li.index(A[key])))
      li.popleft()
      result+=-(len(li)//2-li.index(A[key]))
      key+=1
print(result)